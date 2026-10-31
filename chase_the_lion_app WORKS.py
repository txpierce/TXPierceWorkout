<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TX Pierce Workout & Research Tracker</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        input[type="checkbox"] { accent-color: #f59e0b; }
        /* Hide scrollbars completely while keeping smooth horizontal scrolling */
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen pb-12">

    <!-- HEADER -->
    <header class="bg-slate-900 border-b border-slate-800 sticky top-0 z-50 shadow-lg">
        <div class="max-w-4xl mx-auto px-4 py-2.5 flex items-center justify-between">
            <div class="flex items-center space-x-2">
                <span class="text-xl">🦁</span>
                <div>
                    <h1 class="font-extrabold text-base text-amber-500 tracking-tight leading-none">TX PIERCE APP</h1>
                    <p class="text-[10px] text-slate-400">12-Week Architecture & Peptide Protocol</p>
                </div>
            </div>
            <button onclick="resetData()" class="text-[11px] bg-slate-800 hover:bg-red-950 text-slate-300 hover:text-red-300 px-2.5 py-1 rounded-lg border border-slate-700 transition">Reset Data</button>
        </div>

        <!-- NAVIGATION TABS -->
        <nav class="flex overflow-x-auto px-4 space-x-2 border-t border-slate-800/80 bg-slate-950/50 py-1.5 no-scrollbar">
            <button onclick="switchTab('workouts')" id="btn-workouts" class="tab-btn px-3.5 py-1.5 rounded-xl text-xs font-bold transition whitespace-nowrap bg-amber-500 text-slate-950 shadow-md">Workout Logs</button>
            <button onclick="switchTab('peptides')" id="btn-peptides" class="tab-btn px-3.5 py-1.5 rounded-xl text-xs font-bold transition whitespace-nowrap bg-slate-900 text-slate-400 hover:text-white border border-slate-800">Peptide Tracker</button>
            <button onclick="switchTab('nutrition')" id="btn-nutrition" class="tab-btn px-3.5 py-1.5 rounded-xl text-xs font-bold transition whitespace-nowrap bg-slate-900 text-slate-400 hover:text-white border border-slate-800">Nutrition & Grocery</button>
        </nav>
    </header>

    <main class="max-w-4xl mx-auto px-4 py-4 space-y-4">

        <!-- ================= WORKOUTS TAB ================= -->
        <div id="tab-workouts" class="tab-content active space-y-4">
            
            <!-- PHASE & WEEK SELECTOR -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-3 shadow-xl">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                        <label class="block text-[11px] font-bold text-amber-400 uppercase tracking-wider mb-1">Select Phase</label>
                        <select id="phaseSelect" onchange="changePhase()" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-1.5 text-xs font-semibold text-slate-200 focus:outline-none focus:border-amber-500">
                            <option value="1">Phase 1: Base Phase (Weeks 1-4)</option>
                            <option value="2">Phase 2: Structural Shift (Weeks 5-8)</option>
                            <option value="3">Phase 3: Peak Hypertrophy (Weeks 9-12)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-[11px] font-bold text-amber-400 uppercase tracking-wider mb-1">Select Week</label>
                        <select id="weekSelect" onchange="changeWeek()" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-1.5 text-xs font-semibold text-slate-200 focus:outline-none focus:border-amber-500">
                            <option value="1">Week 1: Baseline</option>
                            <option value="2">Week 2: Progression</option>
                            <option value="3">Week 3: Complexity</option>
                            <option value="4">Week 4: Peak Base</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- DAY SELECTOR BUTTONS (NO SCROLLBAR) -->
            <div class="flex overflow-x-auto space-x-2 py-1 no-scrollbar" id="dayButtonsContainer">
                <!-- Dynamically populated -->
            </div>

            <!-- ACTIVE WORKOUT CARD -->
            <div id="workoutCardContainer" class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-2xl">
                <!-- Dynamically loaded workout table & details -->
            </div>

            <!-- SESSION REVIEW NOTES -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-2">
                <div class="flex items-center space-x-2">
                    <span class="text-amber-500 text-base">📝</span>
                    <h2 class="font-bold text-slate-100 text-xs tracking-wide">Session Review Notes</h2>
                </div>
                <p class="text-[11px] text-slate-400">Log your joint feedback, pump quality, weight increments, or notes for your session review...</p>
                <textarea id="sundayNotes" oninput="saveNotes()" rows="2" placeholder="Write your session review notes here..." class="w-full bg-slate-950 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-200 focus:outline-none focus:border-amber-500"></textarea>
            </div>
        </div>

        <!-- ================= PEPTIDES TAB ================= -->
        <div id="tab-peptides" class="tab-content space-y-4">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl">
                <div class="flex items-center space-x-2 mb-1">
                    <span class="text-amber-500 text-lg">🧪</span>
                    <h2 class="font-extrabold text-slate-100 text-sm">Peptide Reconstitution & Dosing Calculator</h2>
                </div>
                <p class="text-[11px] text-slate-400">Calculate precise BAC water dilution ratios, concentrations, and syringe draw measurements.</p>
            </div>

            <!-- PEPTIDE 1: RETATRUTIDE -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-2 gap-2">
                    <div>
                        <span class="text-[10px] bg-amber-500/10 text-amber-400 font-bold px-2 py-0.5 rounded-md border border-amber-500/20">Iron X Labs</span>
                        <h3 class="font-extrabold text-xs text-slate-100 mt-1">1. Retatrutide (10 mg Vial)</h3>
                    </div>
                    <div class="text-[11px] text-slate-400 bg-slate-950 px-2.5 py-1 rounded-lg border border-slate-800">
                        Target Dose: <strong class="text-amber-400">250 mcg (0.25 mg)</strong>
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80">
                        <label class="block text-[11px] font-bold text-slate-400 mb-1">BAC Water Added (mL)</label>
                        <input type="number" id="reta_bac" value="2.0" step="0.1" oninput="calcReta()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 font-bold text-amber-400 focus:outline-none focus:border-amber-500 text-xs">
                    </div>
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 flex flex-col justify-center">
                        <span class="text-[11px] font-bold text-slate-400">Vial Concentration</span>
                        <span id="reta_conc" class="text-sm font-extrabold text-slate-100 mt-0.5">5.00 mg/mL</span>
                    </div>
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 flex flex-col justify-center">
                        <span class="text-[11px] font-bold text-slate-400">Insulin Syringe Draw (1mL / 100u)</span>
                        <span id="reta_draw" class="text-sm font-extrabold text-amber-400 mt-0.5">5.0 units</span>
                    </div>
                </div>
                <p class="text-[11px] text-slate-400 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/50">
                    💡 <strong>Reference:</strong> 5.0 u = 250 mcg (0.25 mg) | 10.0 u = 500 mcg (0.5 mg) — <span class="text-slate-300">Schedule: Monday Mornings (1x / week)</span>[cite: 5]
                </p>
            </div>

            <!-- PEPTIDE 2: BPC-157 / TB-500 -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-2 gap-2">
                    <div>
                        <span class="text-[10px] bg-amber-500/10 text-amber-400 font-bold px-2 py-0.5 rounded-md border border-amber-500/20">Kingdom Peptides</span>
                        <h3 class="font-extrabold text-xs text-slate-100 mt-1">2. BPC-157 / TB-500 Blend (10 mg Total)</h3>
                    </div>
                    <div class="text-[11px] text-slate-400 bg-slate-950 px-2.5 py-1 rounded-lg border border-slate-800">
                        Target Dose: <strong class="text-amber-400">500 mcg blend</strong>
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80">
                        <label class="block text-[11px] font-bold text-slate-400 mb-1">BAC Water Added (mL)</label>
                        <input type="number" id="bpc_bac" value="2.0" step="0.1" oninput="calcBpc()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 font-bold text-amber-400 focus:outline-none focus:border-amber-500 text-xs">
                    </div>
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 flex flex-col justify-center">
                        <span class="text-[11px] font-bold text-slate-400">Total Blend Conc.</span>
                        <span id="bpc_conc" class="text-sm font-extrabold text-slate-100 mt-0.5">5.00 mg/mL</span>
                    </div>
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 flex flex-col justify-center">
                        <span class="text-[11px] font-bold text-slate-400">Insulin Syringe Draw (1mL / 100u)</span>
                        <span id="bpc_draw" class="text-sm font-extrabold text-amber-400 mt-0.5">10.0 units</span>
                    </div>
                </div>
                <p class="text-[11px] text-slate-400 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/50">
                    💡 <strong>Reference:</strong> 1:1 Ratio (5mg BPC + 5mg TB). 10 units = 500 mcg total blend — <span class="text-slate-300">Schedule: Daily (7 days / week)</span>[cite: 5]
                </p>
            </div>

            <!-- PEPTIDE 3: CJC w/o DAC -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-2 gap-2">
                    <div>
                        <span class="text-[10px] bg-amber-500/10 text-amber-400 font-bold px-2 py-0.5 rounded-md border border-amber-500/20">Iron X Labs</span>
                        <h3 class="font-extrabold text-xs text-slate-100 mt-1">3. CJC w/o DAC (Mod GRF 1-29) (10 mg)</h3>
                    </div>
                    <div class="text-[11px] text-slate-400 bg-slate-950 px-2.5 py-1 rounded-lg border border-slate-800">
                        Target Dose: <strong class="text-amber-400">100 mcg - 200 mcg</strong>
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80">
                        <label class="block text-[11px] font-bold text-slate-400 mb-1">BAC Water Added (mL)</label>
                        <input type="number" id="cjc_bac" value="2.0" step="0.1" oninput="calcCjc()" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 font-bold text-amber-400 focus:outline-none focus:border-amber-500 text-xs">
                    </div>
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 flex flex-col justify-center">
                        <span class="text-[11px] font-bold text-slate-400">Vial Concentration</span>
                        <span id="cjc_conc" class="text-sm font-extrabold text-slate-100 mt-0.5">5.00 mg/mL</span>
                    </div>
                    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 flex flex-col justify-center">
                        <span class="text-[11px] font-bold text-slate-400">Insulin Syringe Draw (1mL / 100u)</span>
                        <span id="cjc_draw" class="text-sm font-extrabold text-amber-400 mt-0.5">2u (100mcg) / 4u (200mcg)</span>
                    </div>
                </div>
                <p class="text-[11px] text-slate-400 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/50">
                    💡 <strong>Reference:</strong> 2 units = 100 mcg | 4 units = 200 mcg (at 2 mL BAC) — <span class="text-slate-300">Schedule: Weeknights (Mon–Fri) before bed</span>[cite: 5]
                </p>
            </div>

            <!-- PEPTIDE WEEKLY SCHEDULER MATRIX -->
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3">
                <div class="flex items-center space-x-2 border-b border-slate-800 pb-2">
                    <span class="text-amber-500 text-lg">📅</span>
                    <h2 class="font-extrabold text-slate-100 text-xs">Weekly Administration Master Matrix</h2>
                </div>
                <div class="overflow-x-auto no-scrollbar">
                    <table class="w-full text-left text-[11px] text-slate-300">
                        <thead class="bg-slate-950 text-slate-400 uppercase font-bold tracking-wider">
                            <tr>
                                <th class="p-2.5 rounded-l-xl">Day</th>
                                <th class="p-2.5">Retatrutide (Weekly)</th>
                                <th class="p-2.5">BPC-157 / TB-500 (Daily)</th>
                                <th class="p-2.5 rounded-r-xl">CJC w/o DAC (Mon-Fri)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60" id="peptideMatrixBody">
                            <!-- Populated via JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ================= NUTRITION TAB ================= -->
        <div id="tab-nutrition" class="tab-content space-y-4">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl">
                <div class="flex items-center space-x-2 mb-1">
                    <span class="text-amber-500 text-lg">🥩</span>
                    <h2 class="font-extrabold text-slate-100 text-sm">Nutrition & Macro Architecture</h2>
                </div>
                <p class="text-[11px] text-slate-400">Targeting ~2,800 Calories daily (200g Protein, 315g Carbohydrates, 80g Fat) optimized for heavy lifting and early morning fueling.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-1.5">
                    <h3 class="font-extrabold text-amber-400 text-xs">1. Pre-Workout (4:15 AM)</h3>
                    <p class="text-[11px] text-slate-300">10g Protein | 30g Carbs (~170 kcal)</p>
                    <p class="text-[11px] text-slate-400">Banana (1 medium) + ½ scoop Whey Protein powder.</p>
                </div>
                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-1.5">
                    <h3 class="font-extrabold text-amber-400 text-xs">2. Post-Workout Breakfast (6:30 AM)</h3>
                    <p class="text-[11px] text-slate-300">40g Protein | 75g Carbs | 15g Fat (~600 kcal)</p>
                    <p class="text-[11px] text-slate-400">2 whole eggs + ¾ cup egg whites, 1 cup dry rolled oats, ½ cup berries.</p>
                </div>
                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-1.5">
                    <h3 class="font-extrabold text-amber-400 text-xs">3. Lunch (12:00 PM)</h3>
                    <p class="text-[11px] text-slate-300">45g Protein | 75g Carbs | 20g Fat (~660 kcal)</p>
                    <p class="text-[11px] text-slate-400">5.0 oz cooked chicken breast, 1.75 cups cooked Jasmine rice, ½ medium avocado.</p>
                </div>
                <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-1.5">
                    <h3 class="font-extrabold text-amber-400 text-xs">4. Afternoon Snack (3:30 PM)</h3>
                    <p class="text-[11px] text-slate-300">35g Protein | 40g Carbs | 15g Fat (~435 kcal)</p>
                    <p class="text-[11px] text-slate-400">1.25 cups Non-Fat Greek Yogurt, 18-20 almonds, 1.5 cups mixed berries.</p>
                </div>
            </div>

            <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl space-y-3">
                <div class="flex items-center space-x-2 border-b border-slate-800 pb-2">
                    <span class="text-amber-500 text-lg">🛒</span>
                    <h2 class="font-extrabold text-slate-100 text-xs">Master Grocery List</h2>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-300">
                    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800/80 space-y-1.5">
                        <h4 class="font-bold text-amber-400 text-xs">🥩 Poultry, Meat & Eggs</h4>
                        <ul class="space-y-1 text-slate-400 list-disc list-inside text-[11px]">
                            <li><strong>Chicken Breast:</strong> 3 lbs raw</li>
                            <li><strong>Top Sirloin / Steak:</strong> 3.5–4 lbs raw</li>
                            <li><strong>Whole Eggs:</strong> 1 carton (18-count)</li>
                            <li><strong>Liquid Egg Whites:</strong> 3 cartons (16 oz)</li>
                            <li><strong>Whey Protein Powder:</strong> 1 tub (2 lb)</li>
                        </ul>
                    </div>
                    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800/80 space-y-1.5">
                        <h4 class="font-bold text-amber-400 text-xs">🍌 Produce & Carbohydrates</h4>
                        <ul class="space-y-1 text-slate-400 list-disc list-inside text-[11px]">
                            <li><strong>Bananas:</strong> 1 bunch (5-6 bananas)</li>
                            <li><strong>Rolled Oats:</strong> 1 container (18 oz+)</li>
                            <li><strong>Jasmine Rice:</strong> 1 bag (2–5 lbs)</li>
                            <li><strong>Sweet Potatoes:</strong> 4 lbs total</li>
                            <li><strong>Fresh/Frozen Berries:</strong> 3-4 containers</li>
                            <li><strong>Avocados:</strong> 4 medium</li>
                            <li><strong>Green Beans:</strong> 3 bags</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <script>
        // Full 12-Week Workout Data Architecture with Day 4 Recovery & Checkable Sets
        const workoutsData = {
            1: { // Phase 1
                1: { // Week 1
                    days: [
                        { name: "Day 1: Push", exercises: [
                            { series: "A-Series", name: "Overhead Press", sets: 5, reps: "5", rest: "2-3 min", rpe: 8, wt: "90 lbs" },
                            { series: "B1", name: "Flat DB Bench Press", sets: 3, reps: "8-10", rest: "-", rpe: 8, wt: "55 lbs" },
                            { series: "B1", name: "Chest-Supported T-Bar Row", sets: 3, reps: "12-15", rest: "90 sec", rpe: 8, wt: "45 lbs" },
                            { series: "B2", name: "Seated DB Arnold Press", sets: 3, reps: "8-10", rest: "-", rpe: 8, wt: "30 lbs" },
                            { series: "B2", name: "Skull Crushers", sets: 3, reps: "6-8", rest: "90 sec", rpe: 8, wt: "80 lbs" },
                            { series: "C-Series", name: "Cable Crossover", sets: 3, reps: "12-15", rest: "-", rpe: 8, wt: "30 lbs" },
                            { series: "C-Series", name: "Tricep Extension", sets: 3, reps: "12-15", rest: "90 sec", rpe: 8, wt: "80 lbs" },
                            { series: "D-Series", name: "DB Lateral Raise → Push-Up", sets: 2, reps: "15-20", rest: "60 sec", rpe: "-", wt: "15 lbs / BW" }
                        ]},
                        { name: "Day 2: Pull", exercises: [
                            { series: "A-Series", name: "Pendlay Row", sets: 4, reps: "6-8", rest: "2-3 min", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "Chin-Up", sets: 3, reps: "AMRAP", rest: "-", rpe: 8, wt: "BW" },
                            { series: "B1", name: "Face Pull", sets: 3, reps: "12-15", rest: "90 sec", rpe: 8, wt: "40 lbs" },
                            { series: "B2", name: "Seated Cable Row", sets: 3, reps: "10-12", rest: "-", rpe: 8, wt: "100 lbs" },
                            { series: "B2", name: "DB Hammer Curl", sets: 3, reps: "10-12", rest: "90 sec", rpe: 8, wt: "25 lbs" },
                            { series: "C-Series", name: "Incline DB Y-Raise", sets: 3, reps: "12-15", rest: "-", rpe: 8, wt: "15 lbs" },
                            { series: "C-Series", name: "EZ Bar Preacher Curl", sets: 3, reps: "12-15", rest: "90 sec", rpe: 8, wt: "40 lbs" },
                            { series: "D-Series", name: "Lat Pulldown → DB Curl", sets: 2, reps: "15-20", rest: "60 sec", rpe: "-", wt: "100 lbs / 25 lbs" }
                        ]},
                        { name: "Day 3: Lower", exercises: [
                            { series: "A-Series", name: "Front Squat", sets: 4, reps: "6-8", rest: "2-3 min", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "Romanian Deadlift", sets: 3, reps: "12-15", rest: "-", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "DB Walking Lunges", sets: 3, reps: "10-12", rest: "90 sec", rpe: 8, wt: "30 lbs" },
                            { series: "B2", name: "Glute Ham Raise", sets: 3, reps: "10-12", rest: "-", rpe: 8, wt: "BW" },
                            { series: "B2", name: "Seated Calf Raise", sets: 3, reps: "12-15", rest: "90 sec", rpe: 8, wt: "90 lbs" },
                            { series: "C-Series", name: "Leg Extension", sets: 3, reps: "15-20", rest: "-", rpe: 8, wt: "50 lbs" },
                            { series: "C-Series", name: "Split Squat ISO Hold", sets: 3, reps: "20-30s", rest: "90 sec", rpe: 8, wt: "BW" }
                        ]},
                        { name: "Day 4: Recovery / Mobility", exercises: [
                            { series: "Warm-Up", name: "Easy Cardio & Diaphragmatic Breaths", sets: 1, reps: "3 min / 5 breaths", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Mobility", name: "Cat-Cow", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Mobility", name: "Thoracic Rotations (Each Side)", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Mobility", name: "Hip Airplanes (Each Side)", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Mobility", name: "Ankle Dorsiflexion Rocks", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Mobility", name: "Band Pull-Aparts & External Rotations", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "Light Band" },
                            { series: "Quality", name: "Bodyweight Squats (Slow) & Hinge Pattern", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Quality", name: "Step-Downs (Each Leg) & Scap Push-Ups", sets: 2, reps: "10 reps", rest: "-", rpe: 3, wt: "BW" },
                            { series: "Cardio", name: "Easy Row or Incline Walk", sets: 1, reps: "10 min", rest: "-", rpe: 3, wt: "Easy" }
                        ]},
                        { name: "Day 5: Upper Pump", exercises: [
                            { series: "A-Series", name: "Incline DB Press", sets: 3, reps: "10-12", rest: "90 sec", rpe: 7, wt: "55 lbs" },
                            { series: "B1", name: "Machine Chest Press", sets: 3, reps: "12-15", rest: "-", rpe: 7, wt: "110 lbs" },
                            { series: "B1", name: "V-Grip Cable Row", sets: 3, reps: "12-15", rest: "90 sec", rpe: 7, wt: "110 lbs" },
                            { series: "B2", name: "Cable Lateral Raise", sets: 3, reps: "15-20", rest: "-", rpe: 7, wt: "20 lbs" },
                            { series: "B2", name: "Tricep Rope Pushdown", sets: 3, reps: "10-12", rest: "90 sec", rpe: 7, wt: "40 lbs" },
                            { series: "C-Series", name: "Straight-Arm Pulldown", sets: 3, reps: "12-15", rest: "-", rpe: 7, wt: "60 lbs" },
                            { series: "C-Series", name: "DB Spider Curl", sets: 3, reps: "12-15", rest: "90 sec", rpe: 7, wt: "25 lbs" }
                        ]},
                        { name: "Day 6: Arms / Calves / Abs", exercises: [
                            { series: "Accessory", name: "Cable Curl", sets: 3, reps: "12-15", rest: "60 sec", rpe: 7, wt: "40 lbs" },
                            { series: "Accessory", name: "Overhead Rope Extension", sets: 3, reps: "12-15", rest: "60 sec", rpe: 7, wt: "40 lbs" },
                            { series: "Accessory", name: "Preacher Curl", sets: 3, reps: "10-12", rest: "60 sec", rpe: 7, wt: "40 lbs" },
                            { series: "Accessory", name: "Bench Dips", sets: 3, reps: "15-20", rest: "60 sec", rpe: 7, wt: "BW" },
                            { series: "Accessory", name: "Standing Calf Raise", sets: 4, reps: "12-15", rest: "60 sec", rpe: 7, wt: "135 lbs" },
                            { series: "Accessory", name: "Hanging Knee Raise", sets: 3, reps: "10-12", rest: "60 sec", rpe: 7, wt: "BW" }
                        ]},
                        { name: "Day 7: Off / Recovery", exercises: [
                            { series: "Recovery", name: "Outdoor Walk & Hydration", sets: 1, reps: "20-30 min", rest: "-", rpe: 2, wt: "BW" }
                        ]}
                    ]
                },
                2: { // Week 2
                    days: [
                        { name: "Day 1: Push", exercises: [
                            { series: "A-Series", name: "Overhead Barbell Press", sets: 5, reps: "6", rest: "2-3 min", rpe: 8, wt: "95 lbs" },
                            { series: "B1", name: "Close-Grip Press", sets: 4, reps: "8-10", rest: "-", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "High-Row", sets: 4, reps: "12-15", rest: "90 sec", rpe: 8, wt: "50 lbs" },
                            { series: "B2", name: "Seated DB Arnold Press", sets: 4, reps: "8-10", rest: "-", rpe: 8, wt: "30 lbs" },
                            { series: "B2", name: "Skull Crushers", sets: 4, reps: "6-8", rest: "90 sec", rpe: 8, wt: "40 lbs" },
                            { series: "C-Series", name: "High-to-Low Fly", sets: 3, reps: "12-15", rest: "-", rpe: 8, wt: "30 lbs" },
                            { series: "C-Series", name: "Rope Overhead", sets: 3, reps: "12-15", rest: "90 sec", rpe: 8, wt: "35 lbs" }
                        ]},
                        { name: "Day 2: Pull", exercises: [
                            { series: "A-Series", name: "Pendlay Row", sets: 4, reps: "6-8", rest: "2-3 min", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "Chin-Up", sets: 4, reps: "AMRAP", rest: "-", rpe: 8, wt: "BW" },
                            { series: "B1", name: "Face Pull", sets: 4, reps: "12-15", rest: "90 sec", rpe: 8, wt: "40 lbs" },
                            { series: "B2", name: "Seated Cable Row", sets: 4, reps: "10-12", rest: "-", rpe: 8, wt: "100 lbs" },
                            { series: "B2", name: "DB Hammer Curl", sets: 4, reps: "10-12", rest: "90 sec", rpe: 8, wt: "25 lbs" }
                        ]},
                        { name: "Day 3: Lower", exercises: [
                            { series: "A-Series", name: "Front Squat", sets: 4, reps: "6-8", rest: "2-3 min", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "Romanian Deadlift", sets: 4, reps: "12-15", rest: "-", rpe: 8, wt: "135 lbs" },
                            { series: "B1", name: "DB Walking Lunges", sets: 4, reps: "10-12", rest: "90 sec", rpe: 8, wt: "30 lbs" },
                            { series: "B2", name: "Glute Ham Raise", sets: 4, reps: "10-12", rest: "-", rpe: 8, wt: "BW" }
                        ]},
                        { name: "Day 4: Recovery / Mobility", exercises: [
                            { series: "Mobility", name: "Mobility Circuit & Diaphragmatic Breaths", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }
                        ]},
                        { name: "Day 5: Upper Pump", exercises: [
                            { series: "A-Series", name: "Incline DB Press", sets: 3, reps: "10-12", rest: "90 sec", rpe: 7, wt: "60 lbs" },
                            { series: "B1", name: "Machine Chest Press", sets: 4, reps: "12-15", rest: "-", rpe: 7, wt: "110 lbs" },
                            { series: "B1", name: "V-Grip Cable Row", sets: 4, reps: "12-15", rest: "90 sec", rpe: 7, wt: "110 lbs" }
                        ]}
                    ]
                },
                3: { // Week 3
                    days: [
                        { name: "Day 1: Push", exercises: [
                            { series: "A-Series", name: "Overhead Barbell Press", sets: 6, reps: "4", rest: "2-3 min", rpe: 9, wt: "100 lbs" },
                            { series: "B1", name: "Incline DB Press", sets: 4, reps: "8-10", rest: "-", rpe: 9, wt: "55 lbs" },
                            { series: "B1", name: "Face Pull", sets: 4, reps: "12-15", rest: "90 sec", rpe: 9, wt: "45 lbs" },
                            { series: "C-Series", name: "Cable Press-Out", sets: 4, reps: "15-20", rest: "90 sec", rpe: 9, wt: "30 lbs" }
                        ]},
                        { name: "Day 2: Pull", exercises: [
                            { series: "A-Series", name: "Pendlay Row", sets: 6, reps: "4", rest: "2-3 min", rpe: 9, wt: "140 lbs" },
                            { series: "B1", name: "Chin-Up", sets: 4, reps: "AMRAP", rest: "-", rpe: 9, wt: "BW" },
                            { series: "C-Series", name: "Incline DB Y-Raise", sets: 4, reps: "15-20", rest: "90 sec", rpe: 9, wt: "15 lbs" }
                        ]},
                        { name: "Day 4: Recovery / Mobility", exercises: [
                            { series: "Mobility", name: "Mobility Circuit & Diaphragmatic Breaths", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }
                        ]}
                    ]
                },
                4: { // Week 4
                    days: [
                        { name: "Day 1: Push", exercises: [
                            { series: "A-Series", name: "Overhead Barbell Press", sets: 4, reps: "8", rest: "2-3 min", rpe: 7, wt: "85 lbs" },
                            { series: "B1", name: "Machine Press", sets: 4, reps: "10-12", rest: "-", rpe: 8, wt: "110 lbs" },
                            { series: "C-Series", name: "Pec Deck", sets: 4, reps: "15-20", rest: "90 sec", rpe: 8, wt: "100 lbs" }
                        ]},
                        { name: "Day 4: Recovery / Mobility", exercises: [
                            { series: "Mobility", name: "Mobility Circuit & Diaphragmatic Breaths", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }
                        ]}
                    ]
                }
            },
            2: { // Phase 2 (Weeks 5-8)
                5: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Barbell Bench Press", sets: 5, reps: "5", rest: "2-3 min", rpe: 8, wt: "135 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] },
                6: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Barbell Bench Press", sets: 4, reps: "8", rest: "2-3 min", rpe: 8, wt: "135 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] },
                7: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Barbell Bench Press", sets: 4, reps: "5", rest: "60-90s", rpe: 8, wt: "135 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] },
                8: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Barbell Bench Press", sets: 3, reps: "10", rest: "2-3 min", rpe: 7, wt: "115 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] }
            },
            3: { // Phase 3 (Weeks 9-12)
                9: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Dumbbell Press", sets: 4, reps: "10", rest: "2 min", rpe: 7, wt: "50 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] },
                10: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Dumbbell Press", sets: 4, reps: "10", rest: "75-90s", rpe: 7, wt: "50 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] },
                11: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Dumbbell Press", sets: 4, reps: "12-15", rest: "90s", rpe: 6, wt: "40 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] },
                12: { days: [
                    { name: "Day 1: Push", exercises: [{ series: "A-Series", name: "Incline Dumbbell Press", sets: 3, reps: "10-12", rest: "90s", rpe: 6, wt: "30 lbs" }] },
                    { name: "Day 4: Recovery / Mobility", exercises: [{ series: "Mobility", name: "Mobility Circuit", sets: 2, reps: "10 reps each", rest: "-", rpe: 3, wt: "BW" }] }
                ] }
            }
        };

        let currentPhase = 1;
        let currentWeek = 1;
        let activeDayIndex = 0;

        window.addEventListener('DOMContentLoaded', () => {
            loadSavedState();
            renderWorkouts();
            renderPeptideMatrix();
            calcReta();
            calcBpc();
            calcCjc();
        });

        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => {
                el.classList.remove('bg-amber-500', 'text-slate-950', 'shadow-md');
                el.classList.add('bg-slate-900', 'text-slate-400', 'border', 'border-slate-800');
            });
            document.getElementById('tab-' + tabId).classList.add('active');
            const activeBtn = document.getElementById('btn-' + tabId);
            activeBtn.classList.remove('bg-slate-900', 'text-slate-400', 'border', 'border-slate-800');
            activeBtn.classList.add('bg-amber-500', 'text-slate-950', 'shadow-md');
        }

        function changePhase() {
            currentPhase = parseInt(document.getElementById('phaseSelect').value);
            const weekSelect = document.getElementById('weekSelect');
            weekSelect.innerHTML = '';
            let startWeek = (currentPhase - 1) * 4 + 1;
            for (let w = startWeek; w < startWeek + 4; w++) {
                let opt = document.createElement('option');
                opt.value = w;
                opt.textContent = `Week ${w}: ` + (w%4 === 1 ? 'Baseline/Shift' : w%4 === 2 ? 'Progression/Volume' : w%4 === 3 ? 'Complexity/Density' : 'Peak/Deload');
                weekSelect.appendChild(opt);
            }
            currentWeek = startWeek;
            activeDayIndex = 0;
            renderWorkouts();
            saveState();
        }

        function changeWeek() {
            currentWeek = parseInt(document.getElementById('weekSelect').value);
            activeDayIndex = 0;
            renderWorkouts();
            saveState();
        }

        function renderWorkouts() {
            const weekObj = workoutsData[currentPhase][currentWeek] || workoutsData[1][1];
            const days = weekObj.days;
            if (activeDayIndex >= days.length) activeDayIndex = 0;

            const dayBtnsContainer = document.getElementById('dayButtonsContainer');
            dayBtnsContainer.innerHTML = '';
            days.forEach((day, idx) => {
                let btn = document.createElement('button');
                btn.onclick = () => { activeDayIndex = idx; renderWorkouts(); };
                btn.className = `px-3 py-1.5 rounded-xl text-xs font-bold transition whitespace-nowrap border ${idx === activeDayIndex ? 'bg-amber-500 text-slate-950 border-amber-500 shadow-md' : 'bg-slate-900 text-slate-300 border-slate-800 hover:bg-slate-800'}`;
                btn.textContent = day.name;
                dayBtnsContainer.appendChild(btn);
            });

            const activeDay = days[activeDayIndex];
            const container = document.getElementById('workoutCardContainer');
            
            let html = `
                <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
                    <div>
                        <span class="text-[10px] text-amber-400 font-bold uppercase tracking-wider">Phase ${currentPhase} • Week ${currentWeek}</span>
                        <h2 class="font-extrabold text-sm text-slate-100 mt-0.5">${activeDay.name}</h2>
                    </div>
                </div>
                <div class="overflow-x-auto no-scrollbar">
                    <table class="w-full text-left text-xs text-slate-300">
                        <thead class="bg-slate-950 text-slate-400 uppercase font-bold tracking-wider text-[10px]">
                            <tr>
                                <th class="p-2 rounded-l-xl">Series</th>
                                <th class="p-2">Exercise</th>
                                <th class="p-2">Sets</th>
                                <th class="p-2">Reps</th>
                                <th class="p-2">Rest</th>
                                <th class="p-2">RPE</th>
                                <th class="p-2">Weight</th>
                                <th class="p-2 rounded-r-xl text-center">Set Tracking</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 text-xs">
            `;

            activeDay.exercises.forEach((ex, exIdx) => {
                const totalSets = parseInt(ex.sets) || 1;
                let checkboxesHtml = `<div class="flex items-center justify-center space-x-1.5">`;
                for (let s = 1; s <= totalSets; s++) {
                    const storageKey = `w_${currentWeek}_d_${activeDayIndex}_ex_${exIdx}_set_${s}`;
                    const isChecked = localStorage.getItem(storageKey) === 'true';
                    checkboxesHtml += `
                        <label class="flex flex-col items-center cursor-pointer text-[9px] text-slate-400">
                            <span>S${s}</span>
                            <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="toggleSet('${storageKey}', this.checked)" class="w-3.5 h-3.5 rounded cursor-pointer mt-0.5">
                        </label>
                    `;
                }
                checkboxesHtml += `</div>`;

                html += `
                    <tr class="hover:bg-slate-950/40 transition">
                        <td class="p-2 font-bold text-amber-400 whitespace-nowrap text-[11px]">${ex.series}</td>
                        <td class="p-2 font-semibold text-slate-200 text-[11px]">${ex.name}</td>
                        <td class="p-2 text-slate-300">${ex.sets}</td>
                        <td class="p-2 text-slate-300">${ex.reps}</td>
                        <td class="p-2 text-slate-400 text-[11px]">${ex.rest}</td>
                        <td class="p-2 text-slate-300">${ex.rpe}</td>
                        <td class="p-2 text-slate-200 font-medium whitespace-nowrap text-[11px]">${ex.wt}</td>
                        <td class="p-2 text-center">${checkboxesHtml}</td>
                    </tr>
                `;
            });

            html += `
                        </tbody>
                    </table>
                </div>
            `;
            container.innerHTML = html;
        }

        function toggleSet(key, val) {
            localStorage.setItem(key, val);
        }

        function calcReta() {
            const bac = parseFloat(document.getElementById('reta_bac').value) || 2.0;
            const vialMg = 10.0;
            const targetMcg = 250;
            const mgPerMl = vialMg / bac;
            const mcgPerUnit = (mgPerMl * 1000) / 100;
            const units = targetMcg / mcgPerUnit;

            document.getElementById('reta_conc').textContent = mgPerMl.toFixed(2) + ' mg/mL';
            document.getElementById('reta_draw').textContent = units.toFixed(1) + ' units';
        }

        function calcBpc() {
            const bac = parseFloat(document.getElementById('bpc_bac').value) || 2.0;
            const vialMg = 10.0;
            const targetMcg = 500;
            const mgPerMl = vialMg / bac;
            const mcgPerUnit = (mgPerMl * 1000) / 100;
            const units = targetMcg / mcgPerUnit;

            document.getElementById('bpc_conc').textContent = mgPerMl.toFixed(2) + ' mg/mL';
            document.getElementById('bpc_draw').textContent = units.toFixed(1) + ' units';
        }

        function calcCjc() {
            const bac = parseFloat(document.getElementById('cjc_bac').value) || 2.0;
            const vialMg = 10.0;
            const mgPerMl = vialMg / bac;
            const mcgPerUnit = (mgPerMl * 1000) / 100;
            const u100 = 100 / mcgPerUnit;
            const u200 = 200 / mcgPerUnit;

            document.getElementById('cjc_conc').textContent = mgPerMl.toFixed(2) + ' mg/mL';
            document.getElementById('cjc_draw').textContent = `${u100.toFixed(1)}u (100mcg) / ${u200.toFixed(1)}u (200mcg)`;
        }

        function renderPeptideMatrix() {
            const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
            const tbody = document.getElementById('peptideMatrixBody');
            tbody.innerHTML = '';
            daysOfWeek.forEach((day, idx) => {
                let reta = idx === 0 ? '🟢 Retatrutide (250mcg / 5u)' : '-';
                let bpc = '🟢 BPC-157 / TB-500 (500mcg / 10u)';
                let cjc = idx < 5 ? '🟢 CJC w/o DAC (100-200mcg / 2-4u)' : '-';
                
                tbody.innerHTML += `
                    <tr class="hover:bg-slate-950/40">
                        <td class="p-2.5 font-bold text-slate-200">${day}</td>
                        <td class="p-2.5 ${idx === 0 ? 'text-amber-400 font-semibold' : 'text-slate-500'}">${reta}</td>
                        <td class="p-2.5 text-slate-300">${bpc}</td>
                        <td class="p-2.5 ${idx < 5 ? 'text-amber-400 font-semibold' : 'text-slate-500'}">${cjc}</td>
                    </tr>
                `;
            });
        }

        function saveNotes() {
            const notes = document.getElementById('sundayNotes').value;
            localStorage.setItem('tx_sunday_notes', notes);
        }

        function saveState() {
            localStorage.setItem('tx_phase', currentPhase);
            localStorage.setItem('tx_week', currentWeek);
        }

        function loadSavedState() {
            const savedPhase = localStorage.getItem('tx_phase');
            const savedWeek = localStorage.getItem('tx_week');
            const savedNotes = localStorage.getItem('tx_sunday_notes');

            if (savedPhase) {
                currentPhase = parseInt(savedPhase);
                document.getElementById('phaseSelect').value = currentPhase;
                changePhase();
            }
            if (savedWeek) {
                currentWeek = parseInt(savedWeek);
                document.getElementById('weekSelect').value = currentWeek;
            }
            if (savedNotes) {
                document.getElementById('sundayNotes').value = savedNotes;
            }
        }

        function resetData() {
            if (confirm('Are you sure you want to reset all workout set checkmarks and saved notes?')) {
                localStorage.clear();
                location.reload();
            }
        }
    </script>
</body>
</html>
```[cite: 5]
