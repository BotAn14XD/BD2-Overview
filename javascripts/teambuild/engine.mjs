const SEVERITY_ORDER = {
  error: 0,
  warning: 1,
  success: 2,
  advice: 3
};

function generateTeamSummary(hasAdvices) {
  if (hasAdvices) {
    return "Team composition looks solid! Review the tactical advice below for specific encounter nuances.";
  }
  return "Team composition looks solid! All Turn 1 requirements are fully met with no warnings.";
}

export function evaluateTeam(team, context, rules) {
  const results = [];
  for (const rule of rules) {
    if (rule.appliesWhen && !rule.appliesWhen(context)) continue;
    const value = rule.check(team, context);
    if (rule.fire(value)) {
      const raw = rule.message(value);
      const messages = Array.isArray(raw) ? raw : [raw];
      for (const message of messages) {
        results.push({ id: rule.id, severity: rule.severity || "warning", message });
      }
    }
  }

  const hasBlockers = results.some(
    (r) => r.severity === "error" || r.severity === "warning"
  );
  const hasAdvices = results.some((r) => r.severity === "advice");

  if (!hasBlockers && team.length > 0) {
    results.push({
      id: "team-all-clear",
      severity: "success",
      message: generateTeamSummary(hasAdvices)
    });
  }

  return results.sort((a, b) => {
    const priorityA = SEVERITY_ORDER[a.severity] ?? 99;
    const priorityB = SEVERITY_ORDER[b.severity] ?? 99;
    return priorityA - priorityB;
  });
}