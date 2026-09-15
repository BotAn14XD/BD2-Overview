const STARTING_SP = 15;
const MULTI_WORD_CHARACTERS = [
  "Sacred Justia",
  "Goblin Slayer",
  "Sword Maiden",
  "High Elf Archer",
  "Kyouka Uzen",
  "Tenka Izumo"
];
const PROPERTY_ADVANTAGE = {
  fire: "Wind",
  wind: "Water",
  water: "Fire",
  light: "Dark",
  dark: "Light"
};

const ELEMENT_ICON_MAP = {
  water: "elementicon1_1",
  fire: "elementicon2_2",
  wind: "elementicon3_3",
  light: "elementicon4_4",
  dark: "elementicon5_5",
  neutral: "elementicon6_6"
};

function renderElementIcon(element) {
  if (!element) return "";
  const key = element.toLowerCase();
  const filename = ELEMENT_ICON_MAP[key];

  if (!filename) return "";
  const iconUrl = new URL(`../../assets/images/battle-system/icons/${filename}.avif`, import.meta.url).href;

  return `<img src="${iconUrl}" alt="${element}" class="icon" loading="lazy" />`;
}

function getCharacterName(unit) {
  if (!unit) return "";
  const name = (unit.name || "").trim();
  const id = (unit.id || "").toLowerCase();

  for (const char of MULTI_WORD_CHARACTERS) {
    const slug = char.toLowerCase().replace(/\s+/g, "_");
    if (name.toLowerCase().endsWith(char.toLowerCase()) || id.endsWith(slug)) {
      return char;
    }
  }

  if (name) {
    const parts = name.split(/\s+/);
    return parts[parts.length - 1];
  }

  if (id) {
    const parts = id.split("_");
    const last = parts[parts.length - 1];
    return last.charAt(0).toUpperCase() + last.slice(1);
  }

  return "";
}

function teamSPRange(team) {
  return team.reduce(
    (totals, u) => ({
      minSP: totals.minSP + (u.minSP || 0),
      maxSP: totals.maxSP + (u.maxSP || 0)
    }),
    { minSP: 0, maxSP: 0 }
  );
}

function calculateUnitChains(team) {
  let activeTeamReinforcements = 0;

  return team.map((unit) => {
    const effects = unit.effects || [];
    const hasTeamReinforce = effects.some((e) => /^chainreinforcement$/i.test(e));
    const hasSelfReinforce = effects.some((e) => /^chainreinforcementself/i.test(e));

    if (hasTeamReinforce) {
      activeTeamReinforcements += 1;
    }

    const totalReinforcements =
      activeTeamReinforcements + (hasSelfReinforce ? 1 : 0);
    const chainsPerHit = 1 + totalReinforcements;
    const baseChains = unit.chains || 0;

    return baseChains * chainsPerHit;
  });
}


const rules = [
  // --- Tier 1: DPS count check ---------------------------------------
  {
    id: "dps-count",
    severity: "warning",
    check: (team) => team.filter((u) => (u.role || []).includes("DPS")).length,
    fire: (count) => count === 0 || count >= 4,
    message: (count) =>
      count === 0
        ? "Your team <strong>does not have DPS</strong> — you will struggle with clearing battles."
        : `Your team consists of <strong>${count} DPS</strong> — this can work early on, but you will quickly struggle with lack of few supports.`
  },

  // --- Tier 1: Turn-order priority check --
  {
    id: "buffer-after-dps",
    severity: "warning",
    check: (team) => {
      return team.filter((unit, idx) => {
        const currentPriority = unit.orderPriority ?? 0;
        return team
          .slice(0, idx)
          .some((prevUnit) => (prevUnit.orderPriority ?? 0) > currentPriority);
      });
    },
    fire: (mismatches) => mismatches.length > 0,
    message: (mismatches) =>
      mismatches
        .map(
          (u) =>
            `<strong>${u.name}</strong> appears after a teammate with higher order priority. Prioritise putting supports first so DPS can rely on their buffs.`
        )
  },

  // --- Tier 1: SP economy - Impossible rotation ----------------------
    {
      id: "sp-economy-impossible",
      severity: "error",
      check: (team) => teamSPRange(team).minSP,
      fire: (minSP) => minSP > STARTING_SP,
      message: (minSP) =>
        `This team requires at least <strong>${minSP} SP</strong> to cast every skill, more than starting <strong>${STARTING_SP} SP</strong>. A full Turn 1 rotation is impossible.`
    },

    // --- Tier 1: SP economy - Upgrade-dependent rotation ---------------
    {
      id: "sp-economy-upgrades-needed",
      severity: "warning",
      check: (team) => teamSPRange(team),
      fire: ({ minSP, maxSP }) => minSP <= STARTING_SP && maxSP > STARTING_SP,
      message: ({ maxSP }) =>
        `This team can consume up to <strong>${maxSP} SP</strong>, more than starting <strong>${STARTING_SP} SP</strong>. Make sure you have dupe upgrades and potential liberation to activate all abilities on Turn 1.`
    },

// --- Tier 1: Matching ATK Amp check ------------
  {
    id: "missing-atk-amp",
    severity: "warning",
    check: (team) => {
      const ampEligibleDPS = team.filter(
        (u) => (u.role || []).includes("DPS")
      );

      // Only count team-wide amps (exclude self-buffs)
      const teamEffects = team.flatMap((u) =>
        (u.effects || []).filter((e) => !/self/i.test(e))
      );

      const hasPhysDPS = ampEligibleDPS.some((u) => u.damageType === "physical");
      const hasMagicDPS = ampEligibleDPS.some((u) => u.damageType === "magic");

      const hasPhysAmp = teamEffects.some((e) => /phys.*amp/i.test(e));
      const hasMagicAmp = teamEffects.some((e) => /magic.*amp/i.test(e));

      const missing = [];
      if (hasPhysDPS && !hasPhysAmp) missing.push("Physical");
      if (hasMagicDPS && !hasMagicAmp) missing.push("Magic");

      return missing;
    },
    fire: (missing) => missing.length > 0,
    message: (missing) =>
      missing.map(
        (type) =>
          `Your team has ${type} DPS but no ${type} ATK buffer. Without this buff, you will be missing a lot of damage.`
      )
  },

  // --- Tier 1: Mismatched support buff check-----
  {
    id: "mismatched-support-amp",
    severity: "warning",
    check: (team) => {
      const ampEligibleDPS = team.filter(
        (u) => (u.role || []).includes("DPS")
      );
      const hasPhysDPS = ampEligibleDPS.some((u) => u.damageType === "physical");
      const hasMagicDPS = ampEligibleDPS.some((u) => u.damageType === "magic");

      return team
        .map((u) => {
          // Exclude self-only buffs
          const teamEffects = (u.effects || []).filter((e) => !/self/i.test(e));
          const hasPhysAmp = teamEffects.some((e) => /phys.*amp/i.test(e));
          const hasMagicAmp = teamEffects.some((e) => /magic.*amp/i.test(e));

          if (hasPhysAmp && hasMagicAmp) {
            if (!hasPhysDPS && !hasMagicDPS && ampEligibleDPS.length > 0) {
              return { unit: u, wastedType: "Physical or Magic" };
            }
            return null;
          }

          if (hasPhysAmp && !hasPhysDPS) {
            return { unit: u, wastedType: "Physical" };
          }

          if (hasMagicAmp && !hasMagicDPS) {
            return { unit: u, wastedType: "Magic" };
          }

          return null;
        })
        .filter(Boolean);
    },
    fire: (mismatches) => mismatches.length > 0,
    message: (mismatches) =>
      mismatches.map(
        ({ unit, wastedType }) =>
          `<strong>${unit.name}</strong> provides ${wastedType} ATK Buff, but the team has no ${wastedType} DPS that benefits from it. Their buff does not impact the damage.`
      )
  },

// --- Tier 1: Duplicate character / costume check --------------------
  {
    id: "duplicate-character",
    severity: "error",
    check: (team) => {
      const charMap = new Map();

      for (const unit of team) {
        const charName = getCharacterName(unit);
        if (!charName) continue;

        if (!charMap.has(charName)) {
          charMap.set(charName, []);
        }
        charMap.get(charName).push(unit.name || unit.id);
      }

      return Array.from(charMap.entries())
        .filter(([_, costumes]) => costumes.length > 1)
        .map(([charName, costumes]) => ({ charName, costumes }));
    },
    fire: (duplicates) => duplicates.length > 0,
    message: (duplicates) =>
      duplicates.map(
        ({ charName, costumes }) =>
          `Your team has multiple costumes of ${charName}. You cannot use different costumes of the same character in a single turn.`
      )
  },

  // --- Tier 2: Damage type synergy check -----
  {
    id: "mixed-damage-type",
    severity: "warning",
    check: (team) => {
      const dps = team.filter((u) => (u.role || []).includes("DPS"));
      return {
        hasPhys: dps.some((u) => u.damageType === "physical"),
        hasMagic: dps.some((u) => u.damageType === "magic")
      };
    },
    fire: ({ hasPhys, hasMagic }) => hasPhys && hasMagic,
    message: () =>
      `Team mixes <strong class="yellow">Physical</strong> and <strong class="magenta">Magical</strong> DPS. It is possible if you run universal buffers, but each <strong class="yellow">ATK</strong> / <strong class="magenta">MATK</strong> buff helps only half of your DPS.`
  },

  // --- Tier 2: AOE targeting profile check ----------------------------
  {
    id: "mixed-aoe-profile",
    severity: "warning",
    check: (team) => {
      const allEffects = team.flatMap((u) => u.effects || []);
      return {
        hasBigAOE: allEffects.some((e) => /^(big|large)aoe$/i.test(e)),
        hasLowAOE: allEffects.some((e) => /^(small|low)aoe$/i.test(e))
      };
    },
    fire: ({ hasBigAOE, hasLowAOE }) => hasBigAOE && hasLowAOE,
    message: () =>
      `Team mixes Big AOE and Low AOE attackers. Combining such DPS can lead to inconsistent clears.`
  },

// --- Tier 2: Elemental counter conditional --------------------------
  {
    id: "conditional-elemental-support-present",
    severity: "warning",
    check: (team) => {
      const propertyBuffers = team.filter((u) =>
        (u.effects || []).includes("propertyDmgAmp")
      );
      if (propertyBuffers.length === 0) return null;

      const dpsList = team.filter((u) => (u.role || []).includes("DPS"));
      
      const targets = dpsList
        .filter((dps) => dps.element && PROPERTY_ADVANTAGE[dps.element.toLowerCase()])
        .map((dps) => ({
          name: dps.name,
          element: dps.element.charAt(0).toUpperCase() + dps.element.slice(1),
          counters: PROPERTY_ADVANTAGE[dps.element.toLowerCase()]
        }));

      const uniqueTargetElements = [...new Set(targets.map((t) => t.counters))];

      return {
        buffers: propertyBuffers,
        targets,
        uniqueTargetElements
      };
    },
    fire: (data) => data !== null,
    message: ({ buffers, targets, uniqueTargetElements }) => {
      if (targets.length === 0) {
        return buffers.map(
          (b) =>
            `${b.name} provides an Elemental Counter Property buff, but the team has no DPS to utilize it.`
        );
      }

      const targetSummary = uniqueTargetElements
        .map((el) => `${renderElementIcon(el)} <strong>${el}</strong>`)
        .join(" and ");

      const breakdown = targets
        .map((t) => `<strong>${t.name} (${renderElementIcon(t.element)} ${t.element})</strong>`)
        .join(", ");

      return buffers.map(
        (b) =>
          `<strong>${b.name}</strong>'s Property buff only activates against weaker property targets. With your current DPS setup [${breakdown}], this buff will only trigger against <strong>${targetSummary}</strong> enemies.`
      );
    }
  },

  // --- Tier 2: Crit rate support check---------
  {
    id: "crit-rate-support",
    severity: "advice",
    check: (team) =>
      team.filter(
        (u) =>
          (u.role || []).includes("buffer") &&
          (u.effects || []).some((e) => /critrate/i.test(e))
      ),
    fire: (critSupports) => critSupports.length < 2,
    message: (critSupports) =>
      critSupports.length === 0
        ? "Your team has no Crit Rate supports. While it is possible to clean battles with no Crit Rate Supports, 2 are adviced for less struggle."
        : `Your team has only 1 Crit Rate support <strong>(${critSupports[0].name})</strong>. While it is absolutely possible to clean battles with 1 Crit Rate support, 2 are adviced for less struggle.`
  },

// --- Tier 2: Conditional chain threshold check (Teresse / Liberta) ---
  {
    id: "conditional-chain-threshold",
    severity: "warning",
    check: (team) => {
      const unitChains = calculateUnitChains(team);
      const warnings = [];

      team.forEach((unit, idx) => {
        const subsequentChains = unitChains
          .slice(idx + 1)
          .reduce((sum, count) => sum + count, 0);

        if (unit.id === "beachside_angel_teresse" && subsequentChains >= 6) {
          warnings.push({
            unit,
            chains: subsequentChains,
            type: "teresse"
          });
        }

        if (unit.id === "onsen_manager_liberta" && subsequentChains <= 9) {
          warnings.push({
            unit,
            chains: subsequentChains,
            type: "liberta"
          });
        }
      });

      return warnings;
    },
    fire: (warnings) => warnings.length > 0,
    message: (warnings) =>
      warnings.map(({ unit, chains, type }) =>
        type === "teresse"
          ? `<strong>${unit.name}</strong>'s buff requires 5 or fewer chains on the target. Teammates acting after her generate ${chains} chains in total — if focused on one enemy, her buff will not apply.`
          : `<strong>${unit.name}</strong>'s buff requires at least 10 chains on the target. Teammates acting after her only generate ${chains} chain(s) in total, so her buff will not trigger.`
      )
  },
  // --- Tier 2: AOE combat profile specialization ---------------------
  {
    id: "aoe-specialization-focus",
    severity: "advice",
    check: (team) => {
      const allEffects = team.flatMap((u) => u.effects || []);
      const hasBigAOE = allEffects.some((e) => /^(big|large)aoe$/i.test(e));
      const hasSmallAOE = allEffects.some((e) =>
        /^(small|low)aoe$|^singletarget$/i.test(e)
      );

      if (hasBigAOE && hasSmallAOE) return null;

      if (hasSmallAOE) return "boss";
      if (hasBigAOE) return "mob-wave";
      return null;
    },
    fire: (focus) => focus !== null,
    message: (focus) =>
      focus === "boss"
        ? "Your team focuses on concentrated damage (Small/Medium AoE). This setup is best suited for single-target and boss encounters, but may struggle to clear regular fights easily."
        : "Your team focuses on wide coverage (Big/Medium AoE). This setup is ideal for AoE fights, but may lack concentrated single-target burst against high-HP bosses."
  },
// --- Tier 2: Turn 1 clear impact check (0 Chains / Summons) ----------
  {
    id: "turn-one-offensive-impact",
    severity: "warning",
    check: (team) => {
      const flagged = [];

      for (const unit of team) {
        const chains = unit.chains ?? 0;
        const effects = unit.effects || [];

        const hasSummon = effects.some((e) => /^summon$/i.test(e));
        const isPreemptive = effects.some((e) => /^preemptive$/i.test(e));

        const providesOffensiveSupport = effects.some(
          (e) =>
            (e.endsWith("Amp") && !/(self|barrier|energyguard|evasion)/i.test(e)) ||
            /(vulnerability|defdebuff|mresdebuff)/i.test(e) ||
            /^(critrate(amp)?|chainreinforcement)$/i.test(e)
        );

        if (chains === 0 && !providesOffensiveSupport && !hasSummon) {
          flagged.push({ unit, type: "no-impact" });
        }

        if (hasSummon) {
          flagged.push({ unit, type: "summon", isPreemptive });
        }
      }

      return flagged;
    },
    fire: (flagged) => flagged.length > 0,
    message: (flagged) =>
      flagged.map(({ unit, type, isPreemptive }) => {
        if (type === "no-impact") {
          return `<strong>${unit.name}</strong> lands no hits and provides no offensive buffs or debuffs, offering no clearing impact on Turn 1.`;
        }
        if (isPreemptive) {
          return `<strong>${unit.name}</strong> relies on a Preemptive Summon. While usable on Turn 1, summons dilute SP compared to direct attackers or dedicated buffers.`;
        }
        return `<strong>${unit.name}</strong> relies on an active Summon. Non-preemptive summons cannot act immediately on Turn 1, offering no direct impact toward an opening clear rotation.`;
      })
  },
{
    id: "sunny-inn-helena-last",
    severity: "warning",
    check: (team) => {
      const helenaIdx = team.findIndex((u) => u.id === "sunny_inn_hand_helena");
      if (helenaIdx === -1) return false;

      const isLast = helenaIdx === team.length - 1;
      const attackersAfter = team
        .slice(helenaIdx + 1)
        .filter((u) => (u.chains || 0) > 0 || (u.role || []).includes("DPS"));

      return isLast || attackersAfter.length === 0;
    },
    fire: (isWasted) => isWasted,
    message: () =>
      `<strong>Sunny Inn Hand Helena</strong> has no attackers acting after her. Her Turn 1 Augmentation is completely wasted unless placed immediately before your DPS/chainers.`
  },
  // --- Tier 2: Conflicting Domain skills check -------------------------
  {
    id: "multiple-domains",
    severity: "warning",
    check: (team) =>
      team.filter((u) => (u.effects || []).some((e) => /^domain$/i.test(e))),
    fire: (domainUnits) => domainUnits.length >= 2,
    message: (domainUnits) => {
      const names = domainUnits.map((u) => `<strong>${u.name}</strong>`).join(" and ");
      return `Your team includes multiple Domain skills (${names}). Only one Domain can be active at a time — the latest applied Domain will overwrite the previous one, wasting the earlier buff.`;
    }
  },
  // --- Tier 2: Pure Fixed Damage DPS check ----------------------------
  {
    id: "fixed-damage-pure-dps",
    severity: "warning",
    check: (team) =>
      team.filter((u) => {
        const roles = u.role || [];
        const isPureDPS = roles.length === 1 && roles[0] === "DPS";
        const hasFixedDamage = (u.effects || []).includes("fixedDamage");
        return isPureDPS && hasFixedDamage;
      }),
    fire: (fixedDps) => fixedDps.length > 0,
    message: (fixedDps) =>
      fixedDps.map(
        (u) =>
          `<strong>${u.name}</strong> relies on Fixed Damage as a DPS. Because Fixed Damage cannot land Critical Hits, their damage ceiling does not scale with Crit buffs and falls off heavily in high-end content.`
      )
  },
// --- Tier 2: Focus Fire target redirection check -------------------
  {
    id: "focus-fire-tactical-note",
    severity: "advice",
    check: (team) =>
      team.filter((u) => (u.effects || []).includes("focusFire")),
    fire: (focusUnits) => focusUnits.length > 0,
    message: (focusUnits) =>
      focusUnits.map(
        (u) =>
          `<strong>${u.name}</strong> applies Focus Fire, redirecting all following attacks to the enemy under the effect. This has zero impact in single-target boss fights, but will redirect AoE patterns in multi-target battles.`
      )
  }
];

export { rules, teamSPRange, STARTING_SP };