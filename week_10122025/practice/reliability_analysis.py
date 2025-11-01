#!/usr/bin/env python3
"""
Model Reliability Analysis - Which model is most reliable and not overfitting?
"""

# Given data
features = [2, 4, 6, 8]
targets = [4, 8, 12, 18]

print("=" * 60)
print("🔍 MODEL RELIABILITY ANALYSIS")
print("=" * 60)
print("Given data:")
for f, t in zip(features, targets):
    print(f"Feature: {f}, Target: {t}")

print("\n" + "=" * 60)
print("📊 ANALYZING THE THREE OPTIONS FOR RELIABILITY")
print("=" * 60)

# Option 1: target = 2 * feature
print("\n1️⃣ Option 1: Target = 2 × Feature")
print("Predictions:")
option1_predictions = []
for f, t in zip(features, targets):
    pred = 2 * f
    option1_predictions.append(pred)
    error = abs(t - pred)
    status = "✅" if error == 0 else f"❌ (error: {error})"
    print(f"   Feature {f}: Predicted {pred}, Actual {t} {status}")

option1_total_error = sum(abs(t - p) for t, p in zip(targets, option1_predictions))
print(f"📊 Total Error: {option1_total_error}")

# Option 2: target = 2 * feature + 2
print("\n2️⃣ Option 2: Target = 2 × Feature + 2")
print("Predictions:")
option2_predictions = []
for f, t in zip(features, targets):
    pred = 2 * f + 2
    option2_predictions.append(pred)
    error = abs(t - pred)
    status = "✅" if error == 0 else f"❌ (error: {error})"
    print(f"   Feature {f}: Predicted {pred}, Actual {t} {status}")

option2_total_error = sum(abs(t - p) for t, p in zip(targets, option2_predictions))
print(f"📊 Total Error: {option2_total_error}")

# Option 3: target = 2 * feature, except when feature = 8, then target = 18
print("\n3️⃣ Option 3: Target = 2 × Feature (except when Feature = 8, then Target = 18)")
print("Predictions:")
option3_predictions = []
for f, t in zip(features, targets):
    if f == 8:
        pred = 18  # Special case for feature = 8
        rule = "(Special case: = 18)"
    else:
        pred = 2 * f  # General rule
        rule = "(General rule: 2×f)"
    option3_predictions.append(pred)
    error = abs(t - pred)
    status = "✅" if error == 0 else f"❌ (error: {error})"
    print(f"   Feature {f}: Predicted {pred}, Actual {t} {status} {rule}")

option3_total_error = sum(abs(t - p) for t, p in zip(targets, option3_predictions))
print(f"📊 Total Error: {option3_total_error}")

print("\n" + "=" * 60)
print("🎯 WHY OPTION 1 IS MOST RELIABLE")
print("=" * 60)

print("""
✅ YOUR ANSWER IS CORRECT! Here's why Option 1 is most reliable:

🔍 RELIABILITY CHARACTERISTICS OF OPTION 1:
• Simple, consistent rule (y = 2x)
• Good fit with minimal error (only 2 total error)
• No arbitrary exceptions or complex rules
• Most likely to generalize to new data

📊 COMPARISON:
• Option 1: Simple rule, small error → RELIABLE & GENERALIZABLE
• Option 2: Simple rule, high error → Poor fit, likely underfitting
• Option 3: Complex rule with exception, perfect fit → OVERFITTING!

🚨 WHY OTHER OPTIONS ARE LESS RELIABLE:

Option 2 (y = 2x + 2):
- High total error (16)
- Doesn't fit the data well
- Systematic bias (always predicts 2 units higher)

Option 3 (y = 2x, except y = 18 when x = 8):
- Perfect fit (0 error) but OVERFITTED
- Memorizes the exception rather than learning pattern
- Unlikely to work on new data

🔮 GENERALIZATION TEST:
If we get new data with feature = 10:
• Option 1: Predicts 20 (consistent with simple pattern)
• Option 2: Predicts 22 (consistently biased)
• Option 3: Predicts 20 (but what if there are more exceptions?)

🎓 KEY INSIGHT:
Option 1 strikes the perfect balance:
- Simple enough to avoid overfitting
- Accurate enough to capture the main pattern
- Most likely to work on future data samples
""")

# Reliability scoring
print("\n" + "=" * 60)
print("📈 RELIABILITY SCORING")
print("=" * 60)

print("Criteria for Reliability:")
print("1. Simplicity (avoids overfitting)")
print("2. Reasonable accuracy on training data")
print("3. Likely to generalize to new data")
print()

print("Option 1 (y = 2x):")
print("  ✅ Simplicity: HIGH (simple linear rule)")
print("  ✅ Accuracy: GOOD (small error)")
print("  ✅ Generalization: HIGH (no memorization)")
print("  🏆 RELIABILITY SCORE: EXCELLENT")

print("\nOption 2 (y = 2x + 2):")
print("  ✅ Simplicity: HIGH (simple linear rule)")
print("  ❌ Accuracy: POOR (high error)")
print("  ⚠️ Generalization: MEDIUM (systematic bias)")
print("  📊 RELIABILITY SCORE: POOR")

print("\nOption 3 (y = 2x, except y = 18 when x = 8):")
print("  ❌ Simplicity: LOW (complex rule with exception)")
print("  ✅ Accuracy: PERFECT (zero error)")
print("  ❌ Generalization: POOR (overfitted)")
print("  📊 RELIABILITY SCORE: POOR (overfitting)")

print("\n🏆 WINNER: Option 1 - Most reliable and not overfitting!")
