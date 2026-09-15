const SEVERITY_ORDER = {
  error: 0,
  warning: 1,
  advice: 2
};

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

  return results.sort((a, b) => {
    const priorityA = SEVERITY_ORDER[a.severity] ?? 99;
    const priorityB = SEVERITY_ORDER[b.severity] ?? 99;
    return priorityA - priorityB;
  });
}