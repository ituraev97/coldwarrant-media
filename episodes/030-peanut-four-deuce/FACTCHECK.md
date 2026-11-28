# FACTCHECK — CASE FILE 030 (independent, 2026-11-28)
Pages re-opened: USAO N.D. Tex. releases (Young sentencing, Feb 28 2025 arrests, Love, Hewitt verdict, Williams sentencing), Fox 4 (Young; Hewitt sentencing; Feb 2025), Dallas Morning News Wilonsky column, Wikipedia Wheatley Place. Word count after edits: 2,539 spoken (>=2,400). LINES=139, all 3-tuples (imported with python3 -I). respell.py unchanged (no names changed).

## Resolved flagged items
- Raybould "impunity": release text = "Today's sentence holds one of its members accountable and sends the clear message that violent gangs will not operate with impunity." Script paraphrase is accurate; graphic labelled paraphrase. OK.
- Hewitt "living in fear": April 10 release, Raybould: "The residents living and working in the Malcolm X Boulevard neighborhood had been living in fear due to the havoc wreaked by..." Script accurate. (Fox 4 Oct 29 has a different Raybould quote, not used.)
- Garner quotes verbatim confirmed (Fox 4 + release). Raybould "Armed gang members... period." confirmed. Bazaldua quote confirmed ("This isn't a secret. This wouldn't be allowed..."; script uses the second sentence only). Hewitt 37+ years, Oct 28 2026 confirmed (Fox 4).
- Plea-date / arrest-day / school conflicts: script already avoids (kept).

## Issues fixed in episode.py
1. "Prosecutors summed it up as intimidation and lawlessness" -> release says the complaints described it; reworded.
2. "Neighbors were saying in 2023 and 2024" (complaint dates not stated) -> "telling investigators".
3. Murders 2023-24 line implied gang responsibility -> added "The release does not say who was responsible."
4. "According to court documents ... so everyone knew who belonged" -> "According to the release ... as a sign of affiliation" (embellishment removed).
5. "The first sentence came in March" (unsourced "first") -> "Love's sentence"; Love "repeat felon" -> release wording "multi-convicted felon"; "about twenty and a half years" (248 mo = 20.7) -> "just under twenty-one".
6. "Three others in the order the courts reached them" (wrong order) -> "three of the others".
7. Williams: "Court records say" -> "The release says"; "two others" -> "two other masked gang members"; "had a Glock" -> "brandished"; "drove off ... led police on chase" -> release wording (fled; got away from police at high speed).
8. Hewitt: "ran a corner store" -> "prosecutors said, ran a storefront"; "prosecutors said evidence showed ... PCP" (PCP not in that sentence of the release) -> release wording on storefronts/residences + codeine in soda; "posts were shown to the jury" (release says posts linked to him) -> "prosecutors said posts linked to him included"; quote-graphic credit changed to match; "a kilogram of PCP" -> "kilogram quantities"; "once again, a live alligator" (could be the same animal) -> "and a live alligator"; "several guns" -> "multiple firearms".
9. Section 924(c): Young's release does not cite the statute -> added that the offense falls under 924; "exactly that count" -> "a count of that kind"; "adds at least five years" hedged "under the statute". Felon-in-possession "not one of them" -> "not listed among them".
10. Guns by brand: now attributed to "the release ... in the charges"; Hellcat/Ruger/FedArm "named in the charges against Young and Love". Young's charge worded "possess with intent to distribute" as in the Feb release.
11. Caiman: Feb release does not say "live" -> "one caiman alligator" (Fox 4 does say live; Hewitt release says live alligator).
12. City lawsuit: "nearby convenience store" -> "a Malcolm X Boulevard convenience store. The suit says..."; "That dispute is not part of this federal case" -> "The federal releases do not mention that dispute"; "the neighborhood was not waiting" -> "the city".
13. "Williams ... Starr, who also presided over Hewitt's trial" unsourced -> removed.
14. Garner: "another important milestone, in" -> "milestone in" (verbatim); "called the sentence" -> "sentencing".
15. Wheatley/Phillis Wheatley phrase aligned to Wikipedia ("first African-American author of a published book of poetry").
16. Closing "Every figure and quote ... DOJ releases and news reports" -> adds public reference sources (Wikipedia, statute).
17. Image dd2/dd3 mismatch: line describing the AR-style pistol on a pillow showed dd3; now dd2.
Other files: thumb_plan Angle A (crop chain + hashtag only, no face: image uncaptioned, identity not stated by DOJ); titles alt 2 "One Boss Man" replaced; description sources add Wikipedia; short.md line 2 attributed to the release.

## Verified without change
Ages 39 / 46 / 23; 300 / 248 / 90 months; 52-month gap; Sept 2025 pleas; Oct 22 2024 seizure quantities (210 g, 4.6 kg PCP, 9.8 g, 1.4 g, 1 kg K2); 14 firearms, >1 kg meth pills, >$47,000, 6 vehicles; 10 agencies; Meacham, Toliver, Calvert, Take Back America; 12 pleaded guilty; Jan 2024 start; Dec 6 2023 Corvette details; 4-day trial, Apr 9 2026; conversions (7.5 oz, ~10 lb, 7.5 yrs, 64, 21 months); Nov 23 2026 = Monday; City suit phrases, Noorani and young-woman comments.

## Residual risks (not fixable by text)
- tv1 (news video of Feb 2025 arrests) is unverified; build agent must watch it, and drop it if it shows faces/commentary/victims. Lines using it are narration only.
- dd1 (uncaptioned social screenshot) is shown many times while Young is discussed; on-screen tag says no caption given. Do not caption the face with his name. Keep handles hidden.
- Williams carjacking victims are unnamed adults; no names used.
- Titles state "He called himself..." as fact; the release states it as fact. Acceptable.

VERDICT: PASS
