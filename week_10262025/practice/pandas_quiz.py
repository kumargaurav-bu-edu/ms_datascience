#!/usr/bin/env python3

"""
Pandas Fundamentals Quiz (Week 9 - DX602)

Learning objectives tested:
- Group data and generate aggregate statistics using pandas
- Filter data using DataFrame queries
- Join data from different DataFrames

Run: python pandas_quiz.py
"""

from __future__ import annotations

import random
from typing import Dict, List, Tuple, Any


class Question:
    def __init__(self, prompt: str, options: Dict[str, str], answer: str, explanation: str):
        self.prompt = prompt
        self.options = options
        self.answer = answer.lower().strip()
        self.explanation = explanation

    def ask(self) -> Tuple[bool, str]:
        print("\n----")
        print(self.prompt)
        for key in sorted(self.options.keys()):
            print(f"  {key}) {self.options[key]}")
        user = input("Your answer: ").strip().lower()
        ok = (user == self.answer)
        return ok, self.explanation


def build_questions() -> List[Question]:
    q: List[Question] = []

    # Groupby & Aggregation (10+)
    q.append(Question(
        "1) Which computes mean body mass by Species?",
        {
            "a": "df.groupby('Species')['Body Mass (g)'].mean()",
            "b": "df['Body Mass (g)'].groupby('Species').median()",
            "c": "df.mean('Species')['Body Mass (g)']",
            "d": "df.groupby('Body Mass (g)')['Species'].mean()",
        },
        "a",
        "Group by key then aggregate target column with mean.",
    ))

    q.append(Question(
        "2) How to keep grouped keys as columns (not index) when averaging?",
        {
            "a": "df.groupby('Species').mean(as_columns=True)",
            "b": "df.groupby('Species', as_index=False).mean()",
            "c": "df.mean().groupby('Species', keep_columns=True)",
            "d": "df.groupby('Species').mean().reset_columns()",
        },
        "b",
        "Use as_index=False to retain group keys as normal columns.",
    ))

    q.append(Question(
        "3) Count penguins per Species (single Series result)?",
        {
            "a": "df['Species'].count()",
            "b": "df.groupby('Species').size()",
            "c": "df.groupby('Species').count()['Species']",
            "d": "df.groupby('Species').nunique()['Species']",
        },
        "b",
        "groupby(...).size() produces a Series of row counts per group.",
    ))

    q.append(Question(
        "4) Which aggregates only numeric columns (pandas 2.x)?",
        {
            "a": "df.groupby('Species').mean(numeric_only=True)",
            "b": "df.groupby('Species').mean(only_numeric=True)",
            "c": "df.numeric().groupby('Species').mean()",
            "d": "df.groupby('Species').mean().numeric_only()",
        },
        "a",
        "mean(numeric_only=True) limits aggregation to numeric dtypes.",
    ))

    q.append(Question(
        "5) Sum cups per recipe/ingredient into wide table (defaults fill 0)?",
        {
            "a": "df.pivot(index='recipe', columns='ingredient', values='cups')",
            "b": "df.pivot_table(index='recipe', columns='ingredient', values='cups', aggfunc='sum', fill_value=0)",
            "c": "df.unstack('ingredient').sum()",
            "d": "df.stack('ingredient').sum()",
        },
        "b",
        "pivot_table with aggfunc='sum' and fill_value=0 is the standard way.",
    ))

    q.append(Question(
        "6) Which gets top-1 group by max of an aggregated column?",
        {
            "a": "g = df.groupby(['Species','Sex'])['Culmen Length (mm)'].mean(); g.idxmax()",
            "b": "df.groupby(['Species','Sex']).max().head(1)",
            "c": "df.max().groupby(['Species','Sex']).head(1)",
            "d": "df.groupby(['Species','Sex'])['Culmen Length (mm)'].nlargest(1)",
        },
        "a",
        "Aggregate then idxmax() on the resulting Series to get the label.",
    ))

    q.append(Question(
        "7) After df.groupby('A').size().reset_index(name='count'), how to set 'A' as index?",
        {
            "a": "df.set_index('A')",
            "b": "df.index = 'A'",
            "c": "df.to_index('A')",
            "d": "df.as_index('A')",
        },
        "a",
        "Use set_index('A') to move the column into the index.",
    ))

    q.append(Question(
        "8) Which returns number of distinct values per group?",
        {
            "a": "df.groupby('Species')['Island'].nunique()",
            "b": "df.groupby('Species')['Island'].size()",
            "c": "df.groupby('Species').unique('Island')",
            "d": "df.groupby('Species')['Island'].distinct()",
        },
        "a",
        "nunique counts unique entries per group.",
    ))

    q.append(Question(
        "9) Which preserves original row order but adds group counts as a column?",
        {
            "a": "df.join(df.groupby('Species').size())",
            "b": "df.merge(df.groupby('Species').size().rename('cnt'), left_on='Species', right_index=True, how='left')",
            "c": "df.groupby('Species').size().reset_index()",
            "d": "df['cnt']=df.groupby('Species').size()",
        },
        "b",
        "Merge back on group key with right_index=True preserves left order.",
    ))

    q.append(Question(
        "10) Which is correct to aggregate multiple functions for one column?",
        {
            "a": "df.groupby('Species')['Body Mass (g)'].agg(['mean','median'])",
            "b": "df.groupby('Species').agg('Body Mass (g)':['mean','median'])",
            "c": "df.agg('Species')['Body Mass (g)':['mean','median']",
            "d": "df.groupby('Species').aggregate({'Body Mass (g)':['unique']})",
        },
        "a",
        "Select the column then .agg([...]) with function names.",
    ))

    # Filtering / Query (10+)
    q.append(Question(
        "11) pandas query: filter Body Mass (g) >= 5000 (proper quoting)?",
        {
            "a": "df.query('Body Mass (g) >= 5000')",
            "b": "df.query('`Body Mass (g)` >= 5000')",
            "c": "df.query(""Body Mass (g) >= 5000"")",
            "d": "df.query('Body_Mass_g >= 5000')",
        },
        "b",
        "Column names with spaces require backticks in query.",
    ))

    q.append(Question(
        "12) Boolean filter (no query): which is correct?",
        {
            "a": "df[df['Sex'] == 'FEMALE' and df['Region'] == 'Anvers']",
            "b": "df[df['Sex'] == 'FEMALE' & df['Region'] == 'Anvers']",
            "c": "df[(df['Sex'] == 'FEMALE') & (df['Region'] == 'Anvers')]",
            "d": "df[df['Sex'].equals('FEMALE') & df['Region'].equals('Anvers')]",
        },
        "c",
        "Use elementwise operators & and parentheses per condition.",
    ))

    q.append(Question(
        "13) Which filters missing values out of column X?",
        {
            "a": "df[df['X'] != None]",
            "b": "df[df['X'].notna()]",
            "c": "df[df['X'].notnull == True]",
            "d": "df.query('X is not None')",
        },
        "b",
        "Use .notna() (or .notnull()) to keep non-missing rows.",
    ))

    q.append(Question(
        "14) Which selects rows where Species is in a list?",
        {
            "a": "df[df['Species'].isin(['Adelie','Gentoo'])]",
            "b": "df[df['Species'] in ['Adelie','Gentoo']]",
            "c": "df.query('Species in [Adelie,Gentoo]')",
            "d": "df.query('Species in Adelie,Gentoo')",
        },
        "a",
        "Use .isin for membership; query requires quoted list items.",
    ))

    q.append(Question(
        "15) Query equivalent of df[(X>=0)&(X<=10)]?",
        {
            "a": "df.query('X in [0,10]')",
            "b": "df.query('X between 0 and 10')",
            "c": "df.query('X >= 0 and X <= 10')",
            "d": "df.query('X >= 0 | X <= 10')",
        },
        "c",
        "between is not a query keyword; use explicit comparisons.",
    ))

    q.append(Question(
        "16) Drop duplicate Islands keeping first occurrence (Series)?",
        {
            "a": "df['Island'].unique()",
            "b": "df['Island'].drop_duplicates()",
            "c": "df['Island'].distinct()",
            "d": "df['Island'].nunique()",
        },
        "b",
        "drop_duplicates returns a Series of unique values in order.",
    ))

    q.append(Question(
        "17) Safest way to update missing ratings from q4 into p4 column without chained assignment warnings?",
        {
            "a": "p4['rating'].update(q4['rating'])",
            "b": "p4.update(q4)",
            "c": "p4['rating'] = p4['rating'].combine_first(q4['rating'])",
            "d": "p4['rating'].fillna(q4['rating'], inplace=True)",
        },
        "c",
        "Assigning combine_first result avoids chained in-place warnings. p4.update also works but can affect multiple columns.",
    ))

    q.append(Question(
        "18) Which returns row count matching a boolean condition most directly?",
        {
            "a": "df[df['X']>0].count()",
            "b": "(df['X']>0).sum()",
            "c": "df.query('X>0').len()",
            "d": "len(df['X']>0)",
        },
        "b",
        "Boolean True evaluates to 1; sum counts matches.",
    ))

    q.append(Question(
        "19) Which negates a boolean mask?",
        {
            "a": "not mask",
            "b": "~mask",
            "c": "!mask",
            "d": "mask.not()",
        },
        "b",
        "Use bitwise NOT ~ for elementwise negation.",
    ))

    q.append(Question(
        "20) Which sorts by 'Rings' ascending then 'Diameter' descending?",
        {
            "a": "df.sort_values(['Rings','Diameter'], ascending=[True, False])",
            "b": "df.sort(['Rings','Diameter'], asc=[True, False])",
            "c": "df.order_by('Rings','Diameter', desc=True)",
            "d": "df.sort_index(['Rings','Diameter'])",
        },
        "a",
        "Sort by multiple columns with list of ascending flags.",
    ))

    # Joins (10+)
    q.append(Question(
        "21) merge vs join: which is true?",
        {
            "a": "merge joins on columns or indexes; join joins on index by default",
            "b": "join is more flexible than merge",
            "c": "merge only supports inner joins",
            "d": "join requires both frames to have identical columns",
        },
        "a",
        "merge is the general API; join is a convenience for index-based joins.",
    ))

    q.append(Question(
        "22) Left join on column 'device' present in both frames?",
        {
            "a": "df_a.join(df_b, on='device', how='left')",
            "b": "df_a.merge(df_b, on='device', how='left')",
            "c": "df_a.concat(df_b, on='device', how='left')",
            "d": "df_a.merge(df_b, left_index=True, right_index=True)",
        },
        "b",
        "Use merge on a shared column key for clarity.",
    ))

    q.append(Question(
        "23) Join df_b by its index to df_a using df_a column 'k'?",
        {
            "a": "df_a.join(df_b, on='k', how='left')",
            "b": "df_a.merge(df_b, on='k', how='left')",
            "c": "df_a.join(df_b.set_index('k'), how='left')",
            "d": "df_a.concat(df_b, axis=1, on='k')",
        },
        "a",
        "join aligns right frame's index to the left's column via on=.",
    ))

    q.append(Question(
        "24) Handle overlapping column names in merge?",
        {
            "a": "Use suffixes=(' _x',' _y')",
            "b": "Use rsuffix only",
            "c": "Overlapping names are not allowed",
            "d": "Rename left only",
        },
        "a",
        "suffixes= is the standard way to disambiguate overlapping columns.",
    ))

    q.append(Question(
        "25) Keep all rows from left even if no match in right?",
        {
            "a": "how='inner'",
            "b": "how='outer'",
            "c": "how='left'",
            "d": "how='right'",
        },
        "c",
        "Left join retains all rows from the left DataFrame.",
    ))

    q.append(Question(
        "26) Merge on different column names: left key 'a', right key 'b'?",
        {
            "a": "df_l.merge(df_r, on='a'=='b')",
            "b": "df_l.merge(df_r, left_on='a', right_on='b', how='left')",
            "c": "df_l.join(df_r, on=('a','b'))",
            "d": "df_l.merge(df_r, left_index=True, right_index=True)",
        },
        "b",
        "Specify left_on and right_on when column names differ.",
    ))

    q.append(Question(
        "27) After two sequential left merges, unmatched values in later files should be?",
        {
            "a": "Filled with 0",
            "b": "Dropped",
            "c": "Left as NaN",
            "d": "Forward-filled",
        },
        "c",
        "Left join keeps rows and uses NaN for missing right-side data.",
    ))

    q.append(Question(
        "28) Convert a cost per component to total device cost with an orders table?",
        {
            "a": "Merge orders→components→costs, then sum quantity*component_cost",
            "b": "Join costs then take mean",
            "c": "Use pivot without merging",
            "d": "Use df.eval('total = component_cost') and sum",
        },
        "a",
        "Standard pipeline: merge to attach costs, compute extended cost, sum.",
    ))

    q.append(Question(
        "29) Which chooses outer join in pandas merge?",
        {
            "a": "how='full'",
            "b": "how='outer'",
            "c": "how='union'",
            "d": "how='both'",
        },
        "b",
        "Outer join keeps the union of keys from both sides.",
    ))

    q.append(Question(
        "30) Best way to append multiple TSV files in order with same columns?",
        {
            "a": "pd.concat([pd.read_csv(f, sep='\t') for f in files], ignore_index=True)",
            "b": "pd.merge([pd.read_csv(f, sep='\t') for f in files])",
            "c": "pd.join([pd.read_csv(f, sep='\t') for f in files])",
            "d": "pd.read_csv(files, sep='\t')",
        },
        "a",
        "Read each then concat in the specified order; ignore_index for clean index.",
    ))

    return q


def print_objectives():
    print("""
Learning objectives
- Group data and compute aggregates with pandas (groupby, agg)
- Filter data using DataFrame queries and boolean masks
- Join data from multiple DataFrames (merge, join)
Key terms: Query, Filtering, Joining
""".strip())


def main():
    print("Pandas Fundamentals Quiz (Week 9 - DX602)")
    print_objectives()
    print("\nInstructions: Answer MCQs by typing the option letter (a/b/c/d).\n")

    questions = build_questions()
    random.shuffle(questions)

    score = 0
    total = len(questions)

    for qu in questions:
        ok, explanation = qu.ask()
        if ok:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Incorrect.")
            print("Explanation:", explanation)

    print("\n==== Summary ====")
    pct = 100.0 * score / total
    print(f"Score: {score}/{total} ({pct:.1f}%)")


if __name__ == "__main__":
    main()


