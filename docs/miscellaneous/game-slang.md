<input type="text" id="slangSearch" onkeyup="filterSlang()" placeholder="Search for slang or full name..." class="slang-search-box">

<div class="quick-filters">
    <button id="btn-Character" onclick="toggleCategory('Character')">Character</button>
    <button id="btn-Content" onclick="toggleCategory('Content')">Content</button>
    <button id="btn-Costume" onclick="toggleCategory('Costume')">Costume</button>
    <button id="btn-Game-Mechanics" onclick="toggleCategory('Game Mechanics')">Game Mechanics</button>
    <button id="btn-Gear" onclick="toggleCategory('Gear')">Gear</button>
    <button id="btn-Resource" onclick="toggleCategory('Resource')">Resource</button>
    <button id="btn-misc" onclick="toggleCategory('Miscellaneous')">Miscellaneous</button>
</div>

<div id="slang-counter" class="slang-counter"></div>

<!-- <div class="alpha-group"> Templates
    # Character
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
    # Content
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
    # Costume
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
    # Game Mechanics
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
    # Gear
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
    # Resource
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
    # Miscellaneous
        <li class="slang-item" data-keywords="">
            <h3></h3>
            <div class="alias-container">
                <span class="alias-tag miscellaneous-tag ignore-exact">Miscellaneous</span>
                <span class="alias-tag"></span>
                <span class="alias-tag rare-tag"></span>
            </div>
            <p></p>
        </li>
</div> -->

<div class="alpha-group"> <!-- A -->
    <h2 class="letter-heading">A</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Ability Skill Books</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Books</span>
                <span class="alias-tag">Ability S. Books</span>
            </div>
            <p>Ability Books is a collective term for ★1 — ★4 Ability Skill Books, used for upgrading Character's Field Ability.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Acting Archbishop Michaela</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bishop</span>
                <span class="alias-tag">Bishop Michaela</span>
                <span class="alias-tag rare-tag">Arch Michaela</span>
                <span class="alias-tag rare-tag">Arch Bish Mich</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Michaela/Acting_Archbishop">Acting Archbishop</a> is one of <a href="https://browndust2.miraheze.org/wiki/Michaela">Michaela's</a> costumes. Used as self-buff costume and weak <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Admiral Sylvia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">ASylvia</span>
                <span class="alias-tag">Adm Sylvia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sylvia/Admiral">Admiral</a> is one of <a href="https://browndust2.miraheze.org/wiki/Sylvia">Sylvia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Adventurer of the Unknown Diana</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">AotU Diana</span>
                <span class="alias-tag">Base Diana</span>
                <span class="alias-tag">Glasses Diana</span>
                <span class="alias-tag rare-tag">AU Diana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Diana/Adventurer_of_the_Unknown">Adventurer of the Unknown</a> is one of <a href="https://browndust2.miraheze.org/wiki/Diana">Diana's</a> costumes. Used as Property Buffer (Support).</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Alice Glacia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Alice</span>
                <span class="alias-tag rare-tag">Fairytale Glacia</span>
                <span class="alias-tag rare-tag">Tank Glacia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Glacia/Alice">Alice</a> is one of <a href="https://browndust2.miraheze.org/wiki/Glacia">Glacia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Tank costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Ancient Crystal</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">AC</span>
                <span class="alias-tag rare-tag">ACrystal</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ancient_Crystal">Ancient Crystal</a> is a resource used for crafting <span class="cross-link" onclick="searchFor('UR')">UR</span> Gear.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Android Queen Lecliss</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">AQ Lecliss</span>
                <span class="alias-tag">Android Lecliss</span>
                <span class="alias-tag rare-tag">Firechip Lecliss</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lecliss/Android_Queen">Android Queen</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lecliss">Lecliss's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Tank costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Angel of Destruction Teresse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">AoD Teresse</span>
                <span class="alias-tag">Base Teresse</span>
                <span class="alias-tag">Angel Teresse</span>
                <span class="alias-tag rare-tag">Knockback Teresse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Teresse/Angel_of_Destruction">Angel of Destruction</a> is one of <a href="https://browndust2.miraheze.org/wiki/Teresse">Teresse's</a> costumes. Used as Knockback unit and <span class="cross-link" onclick="searchFor('SP Battery')">SP Battery</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Anonymous Sage Nartas</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Sage Nartas</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Nartas/Anonymous_Sage">Anonymous Sage</a> is one of <a href="https://browndust2.miraheze.org/wiki/Nartas">Nartas's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Anastasia</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Ana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Anastasia">Anastasia</a> is a playable Fire Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Angelica</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Ange</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Angelica">Angelica</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Anti-Dystopia Diana</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">AD Diana</span>
                <span class="alias-tag">Drunk Diana</span>
                <span class="alias-tag rare-tag">Dystopia Diana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Diana/Anti-Dystopia">Anti-Dystopia</a> is one of <a href="https://browndust2.miraheze.org/wiki/Diana">Diana's</a> costumes. Used as defensive Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Apostle Blade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Blade</span>
                <span class="alias-tag rare-tag">Ablade</span>
                <span class="alias-tag rare-tag">Apblade</span>
                <span class="alias-tag rare-tag">Apos Blade</span>
                <span class="alias-tag rare-tag">Apo Blade</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Blade/Apostle">Apostle</a> is one of <a href="https://browndust2.miraheze.org/wiki/Blade">Blade's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="Morpheah">
            <h3>Apostle Morpeah</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Morpeah</span>
                <span class="alias-tag rare">Apo Morpeah</span>
                <span class="alias-tag rare">Apos Morpeah</span>
                <span class="alias-tag rare">Apo Morpeah</span>
                <span class="alias-tag rare">Apo Morph</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Morpeah/Apostle">Apostle</a> is one of <a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah's</a> costumes. Used as Self-Support Costume and Concentrated Fire Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Apostle Olivier</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">AP Olivier</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olivier/Apostle">Apostle</a> is one of <a href="https://browndust2.miraheze.org/wiki/Olivier">Olivier's</a> costumes. Used as Self-Buffer and <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Attack</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">ATK</span>
            </div>
            <p>Attack is one of in-game stats used mostly by units with Physical damage type to deal damage.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Augmentation</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Aug</span>
                <span class="alias-tag">Amp</span>
            </div>
            <p>Augmentation is a type of Buff that increases Damage of allies, usually with some condition for activation or value.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Awakening Elixir</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Elixir</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Awakening_Elixir">Awakening Elixir</a> is a resource used for Awakening Characters.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- B -->
    <h2 class="letter-heading">B</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>B-Rank Idol Eleaneer</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Idol Ele</span>
                <span class="alias-tag">Idol Eleaneer</span>
                <span class="alias-tag">B-Rank Eleaneer</span>
                <span class="alias-tag rare">B-Rank Ele</span>
                <span class="alias-tag rare-tag">BEle</span>
                <span class="alias-tag rare-tag">Bidol Ele</span>
                <span class="alias-tag rare-tag">Bidol Eleaneer</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eleaneer/B-Rank_Idol">B-Rank Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eleaneer">Eleaneer's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>B-Rank Idol Helena</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">BHelena</span>
                <span class="alias-tag">Bidol Helena</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Helena/B-Rank_Idol">B-Rank Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Helena">Helena's</a> costumes. Used as core Magic Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>B-Rank Idol Seir</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Idol Seir</span>
                <span class="alias-tag rare-tag">Bidol Seir</span>
                <span class="alias-tag rare-tag">B-Rank Seir</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Seir/B-Rank_Idol">B-Rank Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Seir">Seir's</a> costumes. Used as <span class="cross-link" onclick="searchFor('SP Battery')">SP Battery</span></p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>B-Rank Manager Gray</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">B Rank Gray</span>
                <span class="alias-tag">Manager Gray</span>
                <span class="alias-tag rare">Idol Manager Gray</span>
                <span class="alias-tag rare">Idol Gray</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Gray/B-Rank_Manager">B-Rank Manager</a> is one of <a href="https://browndust2.miraheze.org/wiki/Gray">Gray's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Basic Attack</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Normal Attack</span>
            </div>
            <p>Basic Attack is one of possible actions that Character can perform during the Turn. It is single tile attack with no Skill Multiplier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Basic Skill</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">S1</span>
                <span class="alias-tag">S2</span>
                <span class="alias-tag">S3</span>
                <span class="alias-tag">S4</span>
            </div>
            <p>Basic Skill is a Boss Skill that is used by the boss by default. Number represents the display order of said skill.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Beach Vacation Eclipse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Beach Eclipse</span>
                <span class="alias-tag">BV Eclipse</span>
                <span class="alias-tag">Summer Eclipse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eclipse/Beach_Vacation">Beach Vacation</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eclipse">Eclipse's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="Morpheah">
            <h3>Beach Vacation Morpeah</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Beach Morpeah</span>
                <span class="alias-tag">BV Morpeah</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Morpeah/Beach_Vacation">Beach Vacation</a> is one of <a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and <span class="cross-link" onclick="searchFor('Staller')">Staller</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Beachside Angel Teresse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Beach Teresse</span>
                <span class="alias-tag">BTeresse</span>
                <span class="alias-tag">Summer Teresse</span>
                <span class="alias-tag">BA Teresse</span>
                <span class="alias-tag">BATeresse</span>
                <span class="alias-tag rare-tag">Bikini Teresse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Teresse/Beachside_Angel">Beachside Angel</a> is one of <a href="https://browndust2.miraheze.org/wiki/Teresse">Teresse's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Beachside Justice Michaela</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Summer Mich</span>
                <span class="alias-tag">Summer Michaela</span>
                <span class="alias-tag">Beach Mich</span>
                <span class="alias-tag">Beach Michaela</span>
                <span class="alias-tag rare-tag">BJ Mich</span>
                <span class="alias-tag rare-tag">BJ Michaela</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Michaela/Beachside_Justice">Beachside Justice</a> is one of <a href="https://browndust2.miraheze.org/wiki/Michaela">Michaela's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Self-Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Beatrice</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Bea</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Beatrice">Beatrice</a> is a playable Fire Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Bikini Agent Sylvia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bikini Sylvia</span>
                <span class="alias-tag">BA Sylvia</span>
                <span class="alias-tag rare-tag">BA Sylv</span>
                <span class="alias-tag rare-tag">Beach Sylvia</span>
                <span class="alias-tag rare-tag">Summer Sylvia</span>
                <span class="alias-tag rare-tag">Bikini Sylv</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sylvia/Bikini_Agent">Bikini Agent</a> is one of <a href="https://browndust2.miraheze.org/wiki/Sylvia">Sylvia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Bittersweet Bunny Darian</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bunny Darian</span>
                <span class="alias-tag rare-tag">BDarian</span>
                <span class="alias-tag rare-tag">B Darian</span>
                <span class="alias-tag rare-tag">Bunny Durian</span>
                <span class="alias-tag rare-tag">Winter Durian</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Darian/Bittersweet_Bunny">Bittersweet Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Darian">Darian's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DoT')">DoT</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Blade</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Balde</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Blade">Blade</a> is a playable Darkness Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Blood Glutton Justia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">BG Justia</span>
                <span class="alias-tag">Blood Justia</span>
                <span class="alias-tag">Glutton Justia</span>
                <span class="alias-tag rare-tag">BG Justi</span>
                <span class="alias-tag rare-tag">Gluttonous Justia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Justia/Blood_Glutton">Blood Glutton</a> is one of <a href="https://browndust2.miraheze.org/wiki/Justia">Justia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Bomb Fanatic Wiggle</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Wiggle</span>
                <span class="alias-tag rare-tag">Wiggle</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Wiggle/Bomb_Fanatic">Bomb Fanatic</a> is one of <a href="https://browndust2.miraheze.org/wiki/Wiggle">Wiggle's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Bomb in the Hoodie Wiggle</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Hoodie Wiggle</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Wiggle/Bomb_in_the_Hoodie">Bomb in the Hoodie</a> is one of <a href="https://browndust2.miraheze.org/wiki/Wiggle">Wiggle's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Boo Ghost Granhildr</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Boo Gran</span>
                <span class="alias-tag">Ghost Gran</span>
                <span class="alias-tag">Boo Granhildr</span>
                <span class="alias-tag">Ghost Granhildr</span>
                <span class="alias-tag rare-tag">Halloween Gran</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granhildr/Boo_Ghost">Boo Ghost</a> is one of <a href="https://browndust2.miraheze.org/wiki/Granhildr">Granhildr's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvE')">PvE</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Bright Moon Dalvi</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">BM Dalvi</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Dalvi/Bright_Moon">Bright Moon</a> is one of <a href="https://browndust2.miraheze.org/wiki/Dalvi">Dalvi's</a> costumes. Used as weak <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Bunny Spectre</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Bot</span>
                <span class="alias-tag">Robot</span>
                <span class="alias-tag">Summon</span>
                <span class="alias-tag rare-tag">Bunny Robot</span>
            </div>
            <p>Bunny Spectre is a Summon Character from <a href="https://browndust2.miraheze.org/wiki/Morpeah/Daydream_Bunny">Daydream Bunny</a> <a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah</a>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Burst</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">B0</span>
                <span class="alias-tag">B1</span>
                <span class="alias-tag">B2</span>
                <span class="alias-tag">B3</span>
            </div>
            <p>Different <a href="https://botan14xd.github.io/BD2-Overview/character-progression/burst/">Burst</a> Upgrades [Burst 0 (No Burst) — Burst 3 (Maximum Burst)].</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- C -->
    <h2 class="letter-heading">C</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Celebrity Bunny Loen</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bunny Loen</span>
                <span class="alias-tag">CB Loen</span>
                <span class="alias-tag">BLoen</span>
                <span class="alias-tag">B Loen</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Loen/Celebrity_Bunny">Celebrity Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Loen">Loen's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Character Pack</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">Char Pack</span>
                <span class="alias-tag">Cpack</span>
            </div>
            <p>Character Packs are a specific pack type, set in an alternative universe separate from the main story.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Chains</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
            </div>
            <p>A battle mechanic where every hit on an enemy or boss tile applies one chain stack. Each chain stack increases the damage dealt to that enemy by 10%, and they last for one turn before resetting.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Charming Gaze</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag rare-tag">CritDMG / HP% Ring</span>
                <span class="alias-tag rare-tag">HP% Ring</span>
                <span class="alias-tag rare-tag">HP Ring</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Charming_Gaze">Charming Gaze</a> is a UR Craftable Accessory.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Code Name A Rafina</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Code Rafina</span>
                <span class="alias-tag">Code A Rafina</span>
                <span class="alias-tag rare-tag">Spy Raf</span>
                <span class="alias-tag rare-tag">CNA Rafina</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rafina/Code_Name_A">Code Name A</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rafina">Rafina's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DEF')">DEF</span> Shredder.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Code Name O Elise</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Code Elise</span>
                <span class="alias-tag">Code O Elise</span>
                <span class="alias-tag rare-tag">Spy Elise</span>
                <span class="alias-tag rare-tag">CNO Elise</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Elise/Code_Name_O">Code Name O</a> is one of <a href="https://browndust2.miraheze.org/wiki/Elise">Elise's</a> costumes. Used as <span class="cross-link" onclick="searchFor('SP Battery')">SP Battery</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Code Name S Scheherazade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Code S Schera</span>
                <span class="alias-tag">Spy Schera</span>
                <span class="alias-tag rare-tag">Code Schera</span>
                <span class="alias-tag rare-tag">CNS Schera</span>
                <span class="alias-tag">Spy Scheherazade</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scheherazade/Code_Name_S">Code Name S</a> is one of <a href="https://browndust2.miraheze.org/wiki/Scheherazade">Scheherazade's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Comeback Idol Granhildr</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Idol Gran</span>
                <span class="alias-tag">Idol Granhildr</span>
                <span class="alias-tag rare-tag">Comeback Gran</span>
                <span class="alias-tag rare-tag">CI Granhildr</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granhildr/Comeback_Idol">Comeback Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Granhildr">Granhildr's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Tank and Self-Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Comeback Idol Ventana</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Idol Vent</span>
                <span class="alias-tag">Idol Ventana</span>
                <span class="alias-tag rare-tag">CI Ventana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ventana/Comeback_Idol">Comeback Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Ventana">Ventana's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Comeback Idol Yuri</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Idol Yuri</span>
                <span class="alias-tag rare-tag">CI Yuri</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Yuri/Comeback_Idol">Comeback Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Yuri">Yuri's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span></p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Conditional Skill</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">C1</span>
                <span class="alias-tag">C2</span>
                <span class="alias-tag">C3</span>
                <span class="alias-tag">C4</span>
            </div>
            <p>Conditional Skill is a Boss Skill that is triggered whenever the condition is met. Number represents the display order of said skill.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Cooked Rice</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Rice</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Cooked_Rice">Cooked Rice</a> is a Consumable Resource used to obtain Crafting Material, Gold or Slimes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Costume Selective Enhancement</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Unidupe</span>
                <span class="alias-tag">Universal Dupe</span>
                <span class="alias-tag rare-tag">CSE</span>
            </div>
            <p>Costume Selective Enhancement is a resource purchasable from <span class="cross-link" onclick="searchFor('Golden Thread Shop')">Golden Thread Shop</span> that allows the Upgrade of the chosen non-limited Costume.</p>
        </li>
        <li class="slang-item" data-keywords="Critfish">
            <h3>Crit Fish</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
            </div>
            <p>Crit Fish is a mechanic where you restart the turn / battle in order to trigger a <span class="cross-link" onclick="searchFor('Critical Damage')">Critical Damage</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Critical Damage</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Crit DMG</span>
                <span class="alias-tag">CDMG</span>
            </div>
            <p>Critical Damage represents a damage increase for the attack whenever character triggers critical hit.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Critical Rate</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Crit Rate</span>
                <span class="alias-tag">Crate</span>
                <span class="alias-tag">CR</span>
            </div>
            <p>Critical Rate represents a chance that the attack will be a critical one, dealing increased damage.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Crown of Galaxy</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Crown</span>
                <span class="alias-tag">HP% Helm</span>
                <span class="alias-tag">HP Helm</span>
                <span class="alias-tag rare-tag">MRES / HP% Helm</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Crown_of_Galaxy">Crown of Galaxy</a> is a UR Craftable Helmet.</p>
        </li>
            </ul>
</div>

<div class="alpha-group"> <!-- D -->
    <h2 class="letter-heading">D</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Damage Dealer</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">DPS</span>
                <span class="alias-tag rare-tag">DD</span>
            </div>
            <p>Damage Dealer is a Character or Costume that is used to deal massive damage to the enemy.</p>
        </li>
        <li class="slang-item" data-keywords="Burn Frostbite Bleed Rot">
            <h3>Damage Over Time</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">DoT</span>
            </div>
            <p>Damage Over Time is a damage that is being dealt at the end of each round.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Dancing Snowflake Yumi</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">DS Yumi</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Yumi/Dancing_Snowflake">Dancing Snowflake</a> is one of <a href="https://browndust2.miraheze.org/wiki/Yumi">Yumi's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Darian</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Durian</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Darian">Darian</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Dark Knight Lathel</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">DK Lathel</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Mamonir/Dark_Knight">Dark Knight</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lathel">Lathel's</a> costumes. Primarily used as a <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Dark Saintess Liberta</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">DS Liberta</span>
                <span class="alias-tag">Base Liberta</span>
                <span class="alias-tag">Nun Liberta</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liberta/Dark_Saintess">Dark Saintess</a> is one of <a href="https://browndust2.miraheze.org/wiki/Liberta">Liberta's</a> costumes. Used as Physical Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="Morpheah">
            <h3>Daydream Bunny Morpeah</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bunny Morp</span>
                <span class="alias-tag">Bunny Morph</span>
                <span class="alias-tag rare-tag">BMorp</span>
                <span class="alias-tag rare-tag">BMorph</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Morpeah/Daydream_Bunny">Daydream Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and <span class="cross-link" onclick="searchFor('Staller')">Staller</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Deal Snatcher Luvencia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">DS Luv</span>
                <span class="alias-tag">DS Luven</span>
                <span class="alias-tag">DS Luvencia</span>
                <span class="alias-tag">Office Luv</span>
                <span class="alias-tag">Office Luvencia</span>
                <span class="alias-tag rare-tag">Office Luven</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Luvencia/Deal_Snatcher">Deal Snatcher</a> is one of <a href="https://browndust2.miraheze.org/wiki/Luvencia">Luvencia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Death's Shroud</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Flat HP Armor</span>
                <span class="alias-tag rare-tag">MRES / Flat HP Armor</span>
                <span class="alias-tag rare-tag">MRES / HP Armor</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Death's_Shroud">Death's Shroud</a> is a UR Craftable Armor.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Defence</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">DEF</span>
            </div>
            <p>Defense is one of Character's stats that reduces incoming damage from Physical Characters.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Demon's Daughter Seir</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">DD Seir</span>
                <span class="alias-tag">Base Seir</span>
                <span class="alias-tag rare-tag">Demon Seir</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Seir/Demon's_Daughter">Demon's Daughter</a> is one of <a href="https://browndust2.miraheze.org/wiki/Seir">Seir's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Tank.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Demon's Forbidden Book</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag rare-tag">Demon Book</span>
                <span class="alias-tag rare-tag">DFB</span>
                <span class="alias-tag rare-tag">MATK / MATK Weapon</span>
                <span class="alias-tag rare-tag">Double Flat MATK Weapon</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Demon's_Forbidden_Book">Demon's Forbidden Book</a> is a UR Craftable Weapon.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Descendant of the Great Witch Celia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Young Celia</span>
                <span class="alias-tag">Great Witch Celia</span>
                <span class="alias-tag">Descendant Celia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Celia/Descendant_of_the_Great_Witch">Descendant of the Great Witch</a> is one of <a href="https://browndust2.miraheze.org/wiki/Celia">Celia's</a> costumes. Used as Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Desert Flower Sylvia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Sylvia</span>
                <span class="alias-tag">Desert Sylvia</span>
                <span class="alias-tag">Base Sylv</span>
                <span class="alias-tag rare-tag">DF Sylvia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sylvia/Desert_Flower">Desert Flower</a> is one of <a href="https://browndust2.miraheze.org/wiki/Sylvia">Sylvia's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Disciplinary Committee Glacia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">School Glacia</span>
                <span class="alias-tag rare-tag">DC Glacia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Glacia/Disciplinary_Committee">Disciplinary Committee</a> is one of <a href="https://browndust2.miraheze.org/wiki/Glacia">Glacia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>DJ Venaka</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">DJ Ven</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Venaka/DJ">DJ</a> is one of <a href="https://browndust2.miraheze.org/wiki/Venaka">Venaka's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Dragon Scales Protection</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Dragon Scale</span>
                <span class="alias-tag">Flat MATK Glove</span>
                <span class="alias-tag rare-tag">MATK% / MATK Glove</span>
                <span class="alias-tag rare-tag">MATK / Flat MATK Glove</span>
                <span class="alias-tag rare-tag">DSP</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Dragon_Scales_Protection">Dragon Scales Protection</a> is a UR Craftable Glove.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Draw Ticket</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Tix</span>
                <span class="alias-tag">Red Tix</span>
                <span class="alias-tag">Draw Tix</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Draw_Ticket">Draw Ticket</a> is a Resource used to obtain Costumes and Gear.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Dream Bride Eclipse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bride Eclipse</span>
                <span class="alias-tag rare-tag">DB Eclipse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eclipse/Dream_Bride">Dream Bride</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eclipse">Eclipse's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- E -->
    <h2 class="letter-heading">E</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Eclipse</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag rare-tag">Clipse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eclipse">Eclipse</a> is a playable Darkness Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Eleaneer</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Ele</span>
                <span class="alias-tag">Elea</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eleaneer">Eleaneer</a> is a playable Darkness Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Emerging Desire Roxy</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Succubus Roxy</span>
                <span class="alias-tag">ED Roxy</span>
                <span class="alias-tag">Desire Roxy</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Roxy/Emerging_Desire">Emerging Desire</a> is one of <a href="https://browndust2.miraheze.org/wiki/Roxy">Roxy's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
            <li class="slang-item" data-keywords="">
                <h3>Energy Guard</h3>
                <div class="alias-container">
                    <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                    <span class="alias-tag">EG</span>
                    <span class="alias-tag">Shield</span>
                    <span class="alias-tag rare-tag">EGuard</span>
                </div>
                <p>Energy Guard is a Buff that gives temporary <span class="cross-link" onclick="searchFor('HP')">HP</span> that is spent before own Character's <span class="cross-link" onclick="searchFor('HP')">HP</span> upon taking Damage.</p>
            </li>
        <li class="slang-item" data-keywords="">
            <h3>Engraving Scroll</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Scrolls</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Engraving_Scroll">Engraving Scroll</a> is a Resource used for Engraving Characters.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Essences</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
            </div>
            <p>Essences is a collective term for <a href="https://browndust2.miraheze.org/wiki/Essence_of_Perseverance">Essence of Perseverance</a>, <a href="https://browndust2.miraheze.org/wiki/Essence_of_Strength">Essence of Strength</a> and <a href="https://browndust2.miraheze.org/wiki/Essence_of_Life">Essence of Life</a>, used to Engrave a Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Esteemed Adventurer Eris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Eris</span>
                <span class="alias-tag rare-tag">Adv Eris</span>
                <span class="alias-tag rare-tag">EA Eris</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eris/Esteemed_Adventurer">Esteemed Adventurer</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eris">Eris's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Event Pack</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag rare-tag">Epack</span>
            </div>
            <p>Event Packs are a specific pack type, set in an alternative universe separate from the main story.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Evil Castle</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">EC</span>
                <span class="alias-tag">Castle</span>
                <span class="alias-tag rare-tag">ECastle</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle/">Evil Castle</a> is a Content Pack, featuring one time clear and repetitive roguelike content.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Evil Dragon's Blade</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">UR Sword</span>
                <span class="alias-tag rare-tag">CDMG Sword</span>
                <span class="alias-tag rare-tag">ATK / CDMG Weapon</span>
                <span class="alias-tag rare-tag">Crit DMG Sword</span>
                <span class="alias-tag rare-tag">EDB</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Evil_Dragon's_Blade">Evil Dragon's Blade</a> is a UR Craftable Weapon.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Eye of the Destroyer</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag rare-tag">EotD</span>
                <span class="alias-tag rare-tag">MATK / MATK% Weapon</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eye_of_the_Destroyer">Eye of the Destroyer</a> is a UR Craftable Weapon.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- F -->
    <h2 class="letter-heading">F</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Faithful Wings Olivier</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Olivier</span>
                <span class="alias-tag rare-tag">FaithW Olivier</span>
                <span class="alias-tag rare-tag">FW Olivier</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olivier/Faithful_Wings">Faithful Wings</a> is one of <a href="https://browndust2.miraheze.org/wiki/Olivier">Olivier's</a> costumes. Used as <span class="cross-link" onclick="searchFor('SP Battery')">SP Battery</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fallen Wings Olivier</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">FallW Olivier</span>
                <span class="alias-tag rare-tag">FW Olivier</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olivier/Fallen_Wings">Fallen Wings</a> is one of <a href="https://browndust2.miraheze.org/wiki/Olivier">Olivier's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fantasia Square</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">FS</span>
                <span class="alias-tag">Plaza</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/fantasia-square">Fantasia Square</a> is one of the content packs, focused on players interaction with each other, as well as different events held place.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fated Guest</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">FG</span>
                <span class="alias-tag rare-tag">Fated</span>
            </div>
            <p>Fated Guest is a type of Guest in <a href="https://botan14xd.github.io/BD2-Overview/content-packs/glupy-diner/">Glupy Diner</a> that has story and interactive scenes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fiend Guard</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Magic Armor</span>
                <span class="alias-tag">Robe</span>
                <span class="alias-tag">MRES / MRES Armor</span>
                <span class="alias-tag">MRES Armor</span>
                <span class="alias-tag rare-tag">MRES / MRES Robe</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Fiend_Guard">Fiend Guard</a> is a UR Craftable Armor.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fiend Hunter</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">FH</span>
            </div>
            <p>Fiend Hunter is one of the key Game Modes, resolving around defeating a Boss.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fiend Hunt Damage Threshold</h3>
            <div class="alias-container">
                <span class="alias-tag miscellaneous-tag ignore-exact">Miscellaneous</span>
                <span class="alias-tag">Threshold</span>
            </div>
            <p>Threshold is a Minimum Damage required to be dealt in a single fight to achieve given Fiend Hunter Level Clear.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Fire Graffiti Anastasia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">FG Ana</span>
                <span class="alias-tag rare-tag">FG Anastasia</span>
                <span class="alias-tag rare-tag">Fire Graf Ana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Anastasia/Fire_Graffiti">Fire Graffiti</a> is one of <a href="https://browndust2.miraheze.org/wiki/Anastasia">Anastasia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Flat Stat</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Flat HP</span>
                <span class="alias-tag">Flat ATK</span>
                <span class="alias-tag">Flat MATK</span>
                <span class="alias-tag rare-tag">HP+</span>
                <span class="alias-tag rare-tag">ATK+</span>
                <span class="alias-tag rare-tag">MATK+</span>
            </div>
            <p>Flat Stat is a Stat Bonus that is applied before % Bonus and mostly used in Gears.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Frozen Queen Wilhelmina</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">FQ Wilh</span>
                <span class="alias-tag">FQ Wilhelmina</span>
                <span class="alias-tag">Ice Queen Wilh</span>
                <span class="alias-tag">Ice Queen Wilhelmina</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Wilhelmina/Frozen_Queen">Frozen Queen</a> is one of <a href="https://browndust2.miraheze.org/wiki/Wilhelmina">Wilhelmina's</a> costumes. Used as Chainer and Self-Buff Costume.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- G -->
    <h2 class="letter-heading">G</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Game Club Rafina</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">GC Rafina</span>
                <span class="alias-tag">Gamer Rafina</span>
                <span class="alias-tag">Gaming Rafina</span>
                <span class="alias-tag rare-tag">School Rafina</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rafina/Game_Club">Game Club</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rafina">Rafina's</a> costumes. Used as Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Gentle Maid Anastasia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Maid Ana</span>
                <span class="alias-tag">Maid Anastasia</span>
                <span class="alias-tag">Base Ana</span>
                <span class="alias-tag">Base Anastasia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Anastasia/Gentle_Maid">Gentle Maid</a> is one of <a href="https://browndust2.miraheze.org/wiki/Anastasia">Anastasia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Glacia</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag rare-tag">Glac</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Glacia">Glacia</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Glupy Diner</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">Diner</span>
                <span class="alias-tag rare-tag">GD</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/glupy-diner">Glupy Diner</a> is a Content Pack, focused on building your own Diner and interacting with its visitors.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Goblin Slayer</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">GS</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Goblin_Slayer">Goblin Slayer</a> is a playable Fire Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>God-King's Silver Arm</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Silver Arm</span>
                <span class="alias-tag">ATK% Glove</span>
                <span class="alias-tag rare-tag">ATK% / ATK% Glove</span>
                <span class="alias-tag rare-tag">Double ATK% Glove</span>
                <span class="alias-tag rare-tag">GKSA</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/God-King's_Silver_Arm">God-King's Silver Arm</a> is a UR Craftable Glove.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Golden Colosseum</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">GC</span>
                <span class="alias-tag">Colo</span>
                <span class="alias-tag">PvP</span>
                <span class="alias-tag rare-tag">Gcolo</span>
                <span class="alias-tag rare-tag">Coloss</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/golden-colosseum/">Golden Colosseum</a> is a Content Pack, focusing on  <span class="cross-link" onclick="searchFor('PvP')">PvP</span> experience.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Golden Thread</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">GT</span>
                <span class="alias-tag">Thread</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Golden_Thread">Golden Thread</a> is a Resource which is mostly used for obtaining <span class="cross-link" onclick="searchFor('Unidupe')">Unidupe</span> and other Resources. Obtained from getting Costume after already having +5.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Golden Thread Shop</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">GT Shop</span>
                <span class="alias-tag rare-tag">Threads Shop</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Golden_Threads">Powder of Hope</a> Shop is a Shop that uses <span class="cross-link" onclick="searchFor('Golden Thread')">Golden Thread</span> as a currency.</p>
        </li>   
        <li class="slang-item" data-keywords="">
            <h3>Granadair</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Grana</span>
                <span class="alias-tag rare-tag">Gran</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granadair">Granadair</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Granhildr</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Gran</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granhildr">Granhildr</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Guild Raid</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">GR</span>
                <span class="alias-tag rare-tag">GRaid</span>
                <span class="alias-tag rare-tag">G Raid</span>
            </div>
            <p>Guild Raid is a <span class="cross-link" onclick="searchFor('PvE')">PvE</span> type of Content, resolving around killing a Boss and gaining points for the Guild.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- H -->
    <h2 class="letter-heading">H</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Hammer of Thunder</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Hammer</span>
                <span class="alias-tag rare-tag">ATK / ATK% Weapon</span>
                <span class="alias-tag rare-tag">UR Hammer</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Hammer_of_Thunder">Hammer of Thunder</a> is a UR Craftable Weapon.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Helena</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Hel</span>
                <span class="alias-tag rare-tag">Lena</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Helena">Helena</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Helm of Carnage</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Phys Helm</span>
                <span class="alias-tag">DEF / DEF Helm</span>
                <span class="alias-tag">DEF Helm</span>
                <span class="alias-tag rare-tag">Carnage Helm</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Helm_of_Carnage">Helm of Carnage</a> is a UR Craftable Helmet.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Herb Tracker Lathel</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Herbalist Lathel</span>
                <span class="alias-tag rare-tag">HoT Lathel</span>
                <span class="alias-tag rare-tag">HT Lathel</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lathel/Herb_of_Tracker">Herb of Tracker</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lathel">Lathel's</a> costumes. Primarily used as a low Chainer and Sub <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>High Elf Archer</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Archer</span>
                <span class="alias-tag rare-tag">HEA</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/High_Elf_Archer">High Elf Archer</a> is a playable Wind Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Homunculus Lathel</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">HLathel</span>
                <span class="alias-tag">Homo Lathel</span>
                <span class="alias-tag">Homo</span>
                <span class="alias-tag">Homunculus</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lathel/Homunculus">Homunculus</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lathel">Lathel's</a> costumes. Used as a buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Health Points</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">HP</span>
                <span class="alias-tag rare-tag">Health</span>
            </div>
            <p>Health Points represent the character Health. It is used for sustaining enemy damage.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Helm of Death</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">HP% Helm</span>
                <span class="alias-tag">HP Helm</span>
                <span class="alias-tag rare-tag">DEF / HP% Helm</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Helm_of_Death">Helm of Death</a> is a UR Craftable Helmet.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- I -->
    <h2 class="letter-heading">I</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Ikaruga</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Ika</span>
                <span class="alias-tag rare-tag">Ikar</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ikaruga">Ikaruga</a> is a playable Fire Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Immortal Golden Armor</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">HP% Armor</span>
                <span class="alias-tag">HP Armor</span>
                <span class="alias-tag rare-tag">DEF / HP% Armor</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Immortal_Golden_Armor">Immortal Golden Armor</a> is a UR Craftable Armor.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Innocent Bunny Tyr</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bunny Tyr</span>
                <span class="alias-tag rare-tag">BTyr</span>
                <span class="alias-tag rare-tag">IB Tyr</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Tyr/Innocent_Bunny">Innocent Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Tyr">Tyr's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Invulnerable Armor</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Phys Armor</span>
                <span class="alias-tag">DEF / DEF Armor</span>
                <span class="alias-tag">DEF Armor</span>
                <span class="alias-tag rare-tag">Invul Armor</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Invulnerable_Armor">Invulnerable Armor</a> is a UR Craftable Armor.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Iron Monarch Wilhelmina</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">IM Wilh</span>
                <span class="alias-tag">IM Wilhelmina</span>
                <span class="alias-tag">Base Wilh</span>
                <span class="alias-tag">Base Wilhelmina</span>
                <span class="alias-tag rare-tag">Iron Wilh</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Wilhelmina/Iron_Monarch">Iron Monarch</a> is one of <a href="https://browndust2.miraheze.org/wiki/Wilhelmina">Wilhelmina's</a> costumes. Used as Chainer.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- J -->
    <h2 class="letter-heading">J</h2>
    <ul class="slang-list">
    </ul>
</div>

<div class="alpha-group"> <!-- K -->
    <h2 class="letter-heading">K</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Kendo Club Justia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">Kendo Justia</span>
                <span class="alias-tag rare-tag">KC Justia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Justia/Kendo_Club">Kendo Club</a> is one of <a href="https://browndust2.miraheze.org/wiki/Justia">Justia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Killer Doll Lecliss</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Lecliss</span>
                <span class="alias-tag">KD Lecliss</span>
                <span class="alias-tag rare-tag">Doll Lecliss</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lecliss/Killer_Doll">Killer Doll</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lecliss">Lecliss's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Kind Liberator Samay</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Samay</span>
                <span class="alias-tag rare-tag">KL Samay</span>
                <span class="alias-tag rare-tag">Lib Samay</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Samay/Kind_Liberator">Kind Liberator</a> is one of <a href="https://browndust2.miraheze.org/wiki/Samay">Samay's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Kind Student Samay</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Student Samay</span>
                <span class="alias-tag">School Samay</span>
                <span class="alias-tag rare-tag">KS Samay</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Samay/Kind_Student">Kind Student</a> is one of <a href="https://browndust2.miraheze.org/wiki/Samay">Samay's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Knight of Blood Justia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">KoB Justia</span>
                <span class="alias-tag">Base Justia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Justia/Knight_of_Blood">Knight of Blood</a> is one of <a href="https://browndust2.miraheze.org/wiki/Justia">Justia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Knockback</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">KB</span>
            </div>
            <p>Knockback is the one of available actions for a character, allowing to adjust enemy positioning.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- L -->
    <h2 class="letter-heading">L</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Labyrinth Gatekeeper Nebris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Nebris</span>
                <span class="alias-tag rare-tag">Lab Nebris</span>
                <span class="alias-tag rare-tag">Gate Nebris</span>
                <span class="alias-tag rare-tag">Gatekeeper Nebris</span>
                <span class="alias-tag rare-tag">LG Nebris</span>
                <span class="alias-tag rare-tag">Labyrinth Nebris</span>
                <span class="alias-tag rare-tag">Base Neb</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Nebris/Labyrinth_Gatekeeper">Labyrinth Gatekeeper</a> is one of <a href="https://browndust2.miraheze.org/wiki/Nebris">Nebris's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Self-Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Laid-back Lifeguard Nebris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Beach Nebris</span>
                <span class="alias-tag">Summer Nebris</span>
                <span class="alias-tag rare-tag">LBL Nebris</span>
                <span class="alias-tag rare-tag">LL Nebris</span>
                <span class="alias-tag rare-tag">Summer Neb</span>
                <span class="alias-tag rare-tag">Beach Neb</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Nebris/Laid-back_Lifeguard">Laid-back Lifeguard</a> is one of <a href="https://browndust2.miraheze.org/wiki/Nebris">Nebris's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Self-Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Lancelot</h3>
            <div class="alias-container">
                <span class="alias-tag miscellaneous-tag ignore-exact">Miscellaneous</span>
                <span class="alias-tag">Lance</span>
                <span class="alias-tag">Robot</span>
                <span class="alias-tag rare-tag">Lanc</span>
            </div>
            <p>Lancelot is a Support Character in <span class="cross-link" onclick="searchFor('Guild Raid')">Guild Raid</span> that provides unique set of Abilities for a limited amount of Turns.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Last Hope Loen</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Loen</span>
                <span class="alias-tag rare-tag">LH Loen</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Loen/Last_Hope">Last Hope</a> is one of <a href="https://browndust2.miraheze.org/wiki/Loen">Loen's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Last Night</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">LN</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/last-night">Last Night</a> is a Content Pack, focused on the      <span class="cross-link" onclick="searchFor('PvE')">PvE</span> battle with the help of all the roster.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Lecliss</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Lec</span>
                <span class="alias-tag">Leclis</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lecliss">Lecliss</a> is a playable Wind Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Liatris</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Lia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liatris">Liatris</a> is a playable Fire Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Liberated Marauder Kry</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Kry</span>
                <span class="alias-tag rare-tag">Liberator Kry</span>
                <span class="alias-tag rare-tag">LM Kry</span>
                <span class="alias-tag rare-tag">Lib Kry</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Kry/Liberated_Marauder">Liberated Marauder</a> is one of <a href="https://browndust2.miraheze.org/wiki/Kry">Kry's</a> costumes. Used as early <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and <span class="cross-link" onclick="searchFor('DEF')">DEF</span> Shredder.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Liberta</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Lib</span>
                <span class="alias-tag rare-tag">Libe</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liberta">Liberta</a> is a playable Fire Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Little Pumpkin Girl Sonya</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">LPG Sonya</span>
                <span class="alias-tag">Pumpkin Sonya</span>
                <span class="alias-tag">Halloween Sonya</span>
                <span class="alias-tag rare-tag">Pumpkin Tanya</span>
                <span class="alias-tag rare-tag">Halloween Tanya</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sonya/Little_Pumpkin_Girl">Little Pumpkin Girl</a> is one of <a href="https://browndust2.miraheze.org/wiki/Sonya">Sonya's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Lonely Survivor Lathel</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Firechip Lathel</span>
                <span class="alias-tag">LS Lathel</span>
                <span class="alias-tag rare-tag">Apocalypse Lathel</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lathel/Lonely_Survivor">Lonely Survivor</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lathel">Lathel's</a> costumes. Primarily used as a low Chainer and Sub <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Lovely Lady Elise</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Elise</span>
                <span class="alias-tag rare-tag">LL Elise</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Elise/Lovely_Lady">Lovely Lady</a> is one of <a href="https://browndust2.miraheze.org/wiki/Elise">Elise's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DEF')">DEF</span> and <span class="cross-link" onclick="searchFor('MRES')">MRES</span> Shredder.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Loyal Butler Andrew</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">Butler Andrew</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Andrew/Loyal_Butler">Loyal Butler</a> is one of <a href="https://browndust2.miraheze.org/wiki/Andrew">Andrew's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Luvencia</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Luv</span>
                <span class="alias-tag">Luven</span>
                <span class="alias-tag rare-tag">Luva</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Luvencia">Luvencia</a> is a playable Darkness Character.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- M -->
    <h2 class="letter-heading">M</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Magic Amplifier ET001</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Bot</span>
                <span class="alias-tag">Robot</span>
                <span class="alias-tag">Summon</span>
            </div>
            <p>Magic Amplifier ET001 is a Summon Character from <a href="https://browndust2.miraheze.org/wiki/Diana/Magical_Innovator">Magical Innovator</a> <a href="https://browndust2.miraheze.org/wiki/Diana">Diana</a>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Magical Attack</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">MATK</span>
            </div>
            <p>Magical Attack is one of in-game stats used mostly by units with Magical damage type to deal damage.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Magical Innovator Diana</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">MI Diana</span>
                <span class="alias-tag rare-tag">Innovator Diana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Diana/Magical_Innovator">Magical Innovator</a> is one of <a href="https://browndust2.miraheze.org/wiki/Diana">Diana's</a> costumes. Used as Property Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Maid Bikini Rubia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bikini Rubia</span>
                <span class="alias-tag">Summer Rubia</span>
                <span class="alias-tag rare-tag">Beach Rubia</span>
                <span class="alias-tag rare-tag">MB Rubia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rubia/Maid_Bikini">Maid Bikini</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rubia">Rubia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DoT')">DoT</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Maid Name C Rubia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Maid Rubia</span>
                <span class="alias-tag rare-tag">MNC Rubia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rubia/Maid_Name_C">Maid Name C</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rubia">Rubia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('Staller')">Staller</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Maid Name R Liatris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Maid Lia</span>
                <span class="alias-tag">Maid Liatris</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liatris/Maid_Name_R">Maid Name R</a> is one of <a href="https://browndust2.miraheze.org/wiki/Liatris">Liatris's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Mamonir</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Mamo</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Mamonir">Mamonir</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Manga Research Club Jayden</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">MRC Jayden</span>
                <span class="alias-tag rare-tag">Manga Club Jayden</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Jayden/Manga_Research_Club">Manga Research Club</a> is one of <a href="https://browndust2.miraheze.org/wiki/Jayden">Jayden's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Masquerade Bunny Celia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">BCelia</span>
                <span class="alias-tag">Bunny Celia</span>
                <span class="alias-tag rare-tag">Winter Celia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Celia/Masquerade_Bunny">Masquerade Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Celia">Celia's</a> costumes. Used as Chainer and Self-Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Medical Club Teresse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">MC Teresse</span>
                <span class="alias-tag">School Teresse</span>
                <span class="alias-tag">Med Teresse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Teresse/Medical_Club">Medical Club</a> is one of <a href="https://browndust2.miraheze.org/wiki/Teresse">Teresse's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Michaela</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Mich</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Michaela">Michaela</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Miracle Rose Liberta</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Magical Liberta</span>
                <span class="alias-tag rare-tag">MR Liberta</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liberta/Miracle_Rose">Miracle Rose</a> is one of <a href="https://browndust2.miraheze.org/wiki/Liberta">Liberta's</a> costumes. Used as Sub <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Miracle Violet Palette</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Magical Palette</span>
                <span class="alias-tag rare-tag">MV Palette</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Palette/Miracle_Violet">Miracle Violet</a> is one of <a href="https://browndust2.miraheze.org/wiki/Palette">Palette's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Mirror Wars</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">MW</span>
                <span class="alias-tag">Arena</span>
                <span class="alias-tag">PvP</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/mirror-wars/">Mirror Wars</a> is a Content Pack, focusing on  <span class="cross-link" onclick="searchFor('PvP')">PvP</span> experience.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Morpeah</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Morp</span>
                <span class="alias-tag">Morph</span>
                <span class="alias-tag">Morphea</span>
                <span class="alias-tag">Morpheah</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Magical Resistance</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">MRES</span>
            </div>
            <p>Magical Resistance is one of Character's stats that reduces incoming damage from Magical Characters.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- N -->
    <h2 class="letter-heading">N</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Naked Character</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
            </div>
            <p>Naked Character is a Character with no Gear, either unintentionally or on purpose.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Nature's Claw Rou</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">NC Rou</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rou/Nature's_Claw">Nature's Claw</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rou">Rou's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Nebris</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Neb</span>
                <span class="alias-tag">Nebi</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Nebris">Nebris</a> is a playable Wind Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Neon Savior Angelica</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Neon Angelica</span>
                <span class="alias-tag">Neon Ange</span>
                <span class="alias-tag rare-tag">NS Angelica</span>
                <span class="alias-tag rare-tag">NS Ange</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Angelica/Neon_Savior">Neon Savior</a> is one of <a href="https://browndust2.miraheze.org/wiki/Angelica">Angelica's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DoT')">DoT</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Neon Stalker Liatris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Neon Lia</span>
                <span class="alias-tag">Neon Liatris</span>
                <span class="alias-tag rare-tag">NS Lia</span>
                <span class="alias-tag rare-tag">NS Liatris</span>
                <span class="alias-tag rare-tag">Firechip Lia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liatris/Neon_Stalker">Neon Stalker</a> is one of <a href="https://browndust2.miraheze.org/wiki/Liatris">Liatris's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DoT')">DoT</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>New Hire Nebris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">NH Nebris</span>
                <span class="alias-tag">Office Nebris</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Nebris/New_Hire">New Hire</a> is one of <a href="https://browndust2.miraheze.org/wiki/Nebris">Nebris's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>New Hire Seir</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">NH Seir</span>
                <span class="alias-tag">Office Seir</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Seir/New_Hire">New Hire</a> is one of <a href="https://browndust2.miraheze.org/wiki/Seir">Seir's</a> costumes. Used as Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Night of Death Mamonir</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">NoD Mamo</span>
                <span class="alias-tag">Base Mamo</span>
                <span class="alias-tag">Base Mamonir</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Mamonir/Night_of_Death">Night of Death</a> is one of <a href="https://browndust2.miraheze.org/wiki/Mamonir">Mamonir's</a> costumes. Primarily used as a Chainer and <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Night of Jealousy Levia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">NoJ Levia</span>
                <span class="alias-tag">Base Levia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Levia/Night_of_Jealousy">Night of Jealousy</a> is one of <a href="https://browndust2.miraheze.org/wiki/Levia">Levia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Nightmare Bunny Eclipse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bunny Eclipse</span>
                <span class="alias-tag">Beclipse</span>
                <span class="alias-tag rare-tag">NB Eclipse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eclipse/Nightmare_Bunny">Nightmare Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eclipse">Eclipse's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Nuke</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag rare-tag">Burst</span>
            </div>
            <p>Nuke <i>[Noun]</i> — Skill of a Costume that deals massive damage to the enemy all at once.</p>
            <p>Nuke <i>[Verb]</i> — Process of dealing the massive damage to the enemy all at once.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Nuke Turn</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Burst Turn</span>
            </div>
            <p>The specific Turn during a battle where the player deals significantly more damage compared to the rest of the Turns, usually executed after preparing all necessary Buffs and Debuffs.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- O -->
    <h2 class="letter-heading">O</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Olivier</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Oliver</span>
                <span class="alias-tag rare-tag">Olive</span>
                <span class="alias-tag rare-tag">Olive Oil</span>
                <span class="alias-tag rare-tag">Oli</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olivier">Olivier</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Onsen Manager Liberta</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Onsen Liberta</span>
                <span class="alias-tag">Onsen Lib</span>
                <span class="alias-tag">OM Liberta</span>
                <span class="alias-tag rare-tag">OM Lib</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Liberta/Onsen_Manager">Onsen Manager</a> is one of <a href="https://browndust2.miraheze.org/wiki/Liberta">Liberta's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Onsen Practitioner Ventana</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Onsen Ventana</span>
                <span class="alias-tag">Onsen Vent</span>
                <span class="alias-tag rare-tag">OP Ventana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ventana/Onsen_Practitioner">Onsen Practitioner</a> is one of <a href="https://browndust2.miraheze.org/wiki/Ventana">Ventana's</a> costumes. Used as Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Onsen Swordfighter Blade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Onsen Blade</span>
                <span class="alias-tag rare-tag">Onsen Balde</span>
                <span class="alias-tag rare-tag">OS Ventana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Blade/Onsen_Swordfighter">Onsen Swordfighter</a> is one of <a href="https://browndust2.miraheze.org/wiki/Blade">Blade's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Overheat Levia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">OH Levia</span>
                <span class="alias-tag rare-tag">Cyberpunk Levia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Levia/Overheat">Overheat</a> is one of <a href="https://browndust2.miraheze.org/wiki/Levia">Levia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- P -->
    <h2 class="letter-heading">P</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Peerless Javelin</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Javelin</span>
                <span class="alias-tag rare-tag">ATK / ATK Weapon</span>
                <span class="alias-tag rare-tag">Double Flat ATK weapon</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Peerless_Javelin">Peerless Javelin</a> is a UR Craftable Weapon.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Persona of Slander</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Persona</span>
                <span class="alias-tag">Summon</span>
                <span class="alias-tag rare-tag">Light Blue Persona</span>
            </div>
            <p>Persona of Slander is a Summon Character from <a href="https://browndust2.miraheze.org/wiki/Morpeah/Beach_Vacantion">Beach Vacantion</a> <a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah</a>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Persona of Worship</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Persona</span>
                <span class="alias-tag">Summon</span>
            </div>
            <p>Persona of Worship is a Summon Character from <a href="https://browndust2.miraheze.org/wiki/Morpeah/Beach_Vacantion">Beach Vacantion</a> <a href="https://browndust2.miraheze.org/wiki/Morpeah">Morpeah</a>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Piercing Magic Bow Eleaneer</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">Bow Eleaneer</span>
                <span class="alias-tag rare-tag">Bow Ele</span>
                <span class="alias-tag rare-tag">PMB Eleaneer</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eleaneer/Piercing_Magic_Bow">Piercing Magic Bow</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eleaneer">Eleaneer's</a> costumes. Used as Dispel Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Player vs. Environment Content</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">PvE</span>
            </div>
            <p>Player vs. Environment Content resolves around players fighting against environmental enemies.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Player vs. Player Content</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">PvP</span>
            </div>
            <p>Player vs. Player Content resolves around players competing amongst each other directly. Consists of <a href="https://botan14xd.github.io/BD2-Overview/content-packs/mirror-wars">Mirror Wars</a> and <a href="https://botan14xd.github.io/BD2-Overview/content-packs/golden-colosseum/">Golden Colosseum</a>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pool Party Angelica</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PP Ange</span>
                <span class="alias-tag">PP Angelica</span>
                <span class="alias-tag">Pool Angelica</span>
                <span class="alias-tag">Summer Angelica</span>
                <span class="alias-tag rare-tag">Pool Ange</span>
                <span class="alias-tag rare-tag">Summer Ange</span>
                <span class="alias-tag rare-tag">Beach Angelica</span>
                <span class="alias-tag rare-tag">Beach Ange</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Angelica/Pool_Party">Pool Party</a> is one of <a href="https://browndust2.miraheze.org/wiki/Angelica">Angelica's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pool Party Gray</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PP Gray</span>
                <span class="alias-tag">Pool Gray</span>
                <span class="alias-tag">Summer Gray</span>
                <span class="alias-tag rare-tag">Beach Gray</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Gray/Pool_Party">Pool Party</a> is one of <a href="https://browndust2.miraheze.org/wiki/Gray">Gray's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pool Party Justia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PP Justia</span>
                <span class="alias-tag">Pool Justia</span>
                <span class="alias-tag rare-tag">Summer Justia</span>
                <span class="alias-tag rare-tag">Beach Justia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Justia/Pool_Party">Pool Party</a> is one of <a href="https://browndust2.miraheze.org/wiki/Justia">Justia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('Staller')">Staller</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pool Party Lathel</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PP Lathel</span>
                <span class="alias-tag">Pool Lathel</span>
                <span class="alias-tag rare-tag">Summer Lathel</span>
                <span class="alias-tag rare-tag">Beach Lathel</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lathel/Pool_Party">Pool Party</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lathel">Lathel's</a> costumes. Primarily used as a low Chainer and Sub <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pool Party Scheherazade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PP Schera</span>
                <span class="alias-tag">Pool Schera</span>
                <span class="alias-tag">Summer Schera</span>
                <span class="alias-tag rare-tag">PP Schera</span>
                <span class="alias-tag rare-tag">Pool Scheherazade</span>
                <span class="alias-tag rare-tag">Summer Scheherazade</span>
                <span class="alias-tag rare-tag">Beach Schera</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scheherazade/Pool_Party">Pool Party</a> is one of <a href="https://browndust2.miraheze.org/wiki/Scheherazade">Scheherazade's</a> costumes. Used as Dispel Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Poolside Fairy Refithea</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PF Refi</span>
                <span class="alias-tag">PP Refi</span>                
                <span class="alias-tag">Pool Refi</span>
                <span class="alias-tag">Summer Refi</span>
                <span class="alias-tag rare-tag">Pool Refithea</span>
                <span class="alias-tag rare-tag">Summer Refithea</span>
                <span class="alias-tag rare-tag">Beach Refi</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refithea/Poolside_Fairy">Poolside Fairy</a> is one of <a href="https://browndust2.miraheze.org/wiki/Refithea">Refithea's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Poolside Guardian Zenith</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PG Zenith</span>
                <span class="alias-tag">Pool Zenith</span>
                <span class="alias-tag">Summer Zenith</span>
                <span class="alias-tag rare-tag">Beach Zenith</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Zenith/Poolside_Guardian">Poolside Guardian</a> is one of <a href="https://browndust2.miraheze.org/wiki/Zenith">Zenith's</a> costumes. Used as Chainer and Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Potential Liberation</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Pots</span>
                <span class="alias-tag rare-tag">Potlib</span>
                <span class="alias-tag rare-tag">Tree</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/character-progression/potential-liberation/">Potential Liberation</a> is a character progression feature offering stats increase as well as direct skill enhancement.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Powder of Hope</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">PoH</span>
                <span class="alias-tag">Powder</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Powder_of_Hope">Powder of Hope</a> is a Resource which is mostly used for obtaining Costumes. Obtained from Draw System.</p>
            <p>Powder <i>[Verb]</i> — to buy a Costume from <span class="cross-link" onclick="searchFor('Powder of Hope Shop')">Powder of Hope Shop</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Powder of Hope Shop</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">PoH Shop</span>
                <span class="alias-tag rare-tag">PShop</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Powder_of_Hope">Powder of Hope Shop</a> is a Shop that uses <span class="cross-link" onclick="searchFor('Powder of Hope')">Powder of Hope</span> as a currency.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pressure</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
            </div>
            <p>Pressure is a Debuff that decreases Buff Efficiency. Refer to <a href="https://botan14xd.github.io/BD2-Overview/game-mechanics/damage-formula/#__tabbed_1_4">Damage Formula</a> Page for more information.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Priestess</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Priest</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Priestess">Priestess</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Prime Authority</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Prime</span>
                <span class="alias-tag">Flat ATK Glove</span>
                <span class="alias-tag rare-tag">ATK% / ATK Glove</span>
                <span class="alias-tag rare-tag">ATK / Flat ATK Glove</span>
                <span class="alias-tag rare-tag">PA</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Prime_Authority">Prime Authority</a> is a UR Craftable Glove.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Promise of Harmony</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag rare-tag">CRate / HP% Accessory</span>
                <span class="alias-tag rare-tag">CRate / HP% Necklace</span>
                <span class="alias-tag rare-tag">CR / HP% Accessory</span>
                <span class="alias-tag rare-tag">CR / HP% Necklace</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Promise_of_Harmony">Promise of Harmony</a> is a UR Craftable Accessory.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Promise of Vengeance Lathel</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PoV Lathel</span>
                <span class="alias-tag">Vengeance Lathel</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Lathel/Promise_of_Vengeance">Promise of Vengeance</a> is one of <a href="https://browndust2.miraheze.org/wiki/Lathel">Lathel's</a> costumes. Primarily used as a <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Property</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Prop</span>
                <span class="alias-tag">Element</span>
            </div>
            <p>Property is one of the character's traits that increases damage dealt versus weaker Property and reduces damage dealt versus a stronger one.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Property Crystal</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Water Crystal</span>
                <span class="alias-tag">Fire Crystal</span>
                <span class="alias-tag">Wind Crystal</span>
                <span class="alias-tag">Light Crystal</span>
                <span class="alias-tag">Dark Crystal</span>
            </div>
            <p>Property Crystal is a collective term for the various elemental crystals (Water, Fire, Wind, Light, and Darkness) used for <a href="https://botan14xd.github.io/BD2-Overview/character-progression/potential-liberation/">Potential Liberation</a> of a Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Property Damage</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Prop Damage</span>
            </div>
            <p>Damage buffed with <span class="cross-link" onclick="searchFor('Property')">Property</span> Advantage.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Property Selective Draw Exchange Ticket</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Property Ticket</span>
                <span class="alias-tag">Prop Tix</span>
                <span class="alias-tag">Proptix</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Property_Selective_Draw_Exchange_Ticket">Property Selective Draw Exchange Ticket</a> is a Resource that used to obtain Costumes from chosen <span class="cross-link" onclick="searchFor('Property')">Property</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Prophetic Dream Darian</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Darian</span>
                <span class="alias-tag rare-tag">PD Darian</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Darian/Prophetic_Dream">Prophetic Dream</a> is one of <a href="https://browndust2.miraheze.org/wiki/Darian">Darian's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Pure White Blessing Refithea</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">PWB Refi</span>
                <span class="alias-tag">BRefi</span>
                <span class="alias-tag">Bride Refi</span>
                <span class="alias-tag">Bride Refithea</span>
                <span class="alias-tag rare-tag">PWB Refithea</span>
                <span class="alias-tag rare-tag">BRefithea</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refithea/Pure_White_Blessing">Pure White Blessing</a> is one of <a href="https://browndust2.miraheze.org/wiki/Refithea">Refithea's</a> costumes. Used as Buffer.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- Q -->
    <h2 class="letter-heading">Q</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Queen of Gluttis Granadair</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">QoG Grana</span>
                <span class="alias-tag">Base Grana</span>
                <span class="alias-tag">QoG Granadair</span>
                <span class="alias-tag">Base Granadair</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granadair/Queen_of_Gluttis">Queen of Gluttis</a> is one of <a href="https://browndust2.miraheze.org/wiki/Granadair">Granadair's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Queen of Signatures Michaela</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">QoS Michaela</span>
                <span class="alias-tag">Office Michaela</span>
                <span class="alias-tag rare-tag">QoS Mich</span>
                <span class="alias-tag rare-tag">Office Mich</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Michaela/Queen_of_Signatures">Queen of Signatures</a> is one of <a href="https://browndust2.miraheze.org/wiki/Michaela">Michaela's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- R -->
    <h2 class="letter-heading">R</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Rafina</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Raf</span>
            </div>
            <p><a   href="https://browndust2.miraheze.org/wiki/Rafina">Rafina</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Rebellion</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">CR Glove</span>
                <span class="alias-tag">Crit Rate Glove</span>
                <span class="alias-tag">Crit Glove</span>
                <span class="alias-tag rare-tag">CritRate Glove</span>
                <span class="alias-tag rare-tag">ATK / CR Glove</span>
                <span class="alias-tag rare-tag">ATK / CRate Glove</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rebellion">Rebellion</a> is a UR Craftable Glove.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Recommended ★5 Costume Selective Ticket</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Rainbow Tix</span>
                <span class="alias-tag">Rainbow Ticket</span>
                <span class="alias-tag">Selective Ticket</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Recommended_5-Star_Costume_Selective_Ticket">Recommended ★5 Costume Selective Ticket</a> is a Resource allowing you to choose one Costume out of suggested 12. </p>
        </li>
        <li class="slang-item" data-keywords="Scrolls">
            <h3>Recruitment Contract</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">R. Contract</span>
                <span class="alias-tag">Scroll</span>
            </div>
            <p>Recruitment Contract is a collective term for ★3, ★4 and ★5 Contracts, used for recruiting Costumes from Pub.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Red Riding Hood Rou</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">RRH Rou</span>
                <span class="alias-tag">Red Hat Rou</span>
                <span class="alias-tag rare-tag">Red Rou</span>
                <span class="alias-tag rare-tag">RR Rou</span>
                <span class="alias-tag rare-tag">RRou</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rou/Red_Riding_Hood">Red Riding Hood</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rou">Rou's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Refining Crystal</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">RC</span>
                <span class="alias-tag rare-tag">Ref Crystal</span>
                <span class="alias-tag rare-tag">RCrystal</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refining_Crystal">Refining Crystal</a> is a Resource used to change <span class="cross-link" onclick="searchFor('Substats')">Substats</span> of the gear.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Refining Powder</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Powder</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refining_Powder">Refining Powder</a> is a Resource used to upgrade Gear.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Refining Stone</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">RS</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refining_Stone">Refining Stone</a> <!--STUB--></p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Refithea</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Refi</span>
                <span class="alias-tag">Ref</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refithea">Refithea</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Respected Master Roxy</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Roxy</span>
                <span class="alias-tag rare-tag">RM Roxy</span>
                <span class="alias-tag rare-tag">Master Roxy</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Roxy/Respected_Master">Respected Master</a> is one of <a href="https://browndust2.miraheze.org/wiki/Roxy">Roxy's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Retired Legend Olivier</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">RL Olivier</span>
                <span class="alias-tag rare-tag">Retired Olivier</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olivier/Retired_Legend">Retired Legend</a> is one of <a href="https://browndust2.miraheze.org/wiki/Olivier">Olivier's</a> costumes. Used as Buffer and Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Rigenette</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Rigen</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rigenette">Rigenette</a> is a playable Wind Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Ring of Fury</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">CR Glove</span>
                <span class="alias-tag">Crit Rate Glove</span>
                <span class="alias-tag">Crit Glove</span>
                <span class="alias-tag rare-tag">CritRate Glove</span>
                <span class="alias-tag rare-tag">MATK / CR Glove</span>
                <span class="alias-tag rare-tag">MATK / CRate Glove</span>
                <span class="alias-tag rare-tag">RoF</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ring_of_Fury">Ring of Fury</a> is a UR Craftable Glove.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Ring of the Lake</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag rare-tag">Flat HP Ring</span>
                <span class="alias-tag rare-tag">CDMG / HP Ring</span>
                <span class="alias-tag rare-tag">CritDMG / HP Ring</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ring_of_the_Lake">Ring of the Lake</a> is a UR Craftable Accessory.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Robin Hood Zenith</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">RH Zenith</span>
                <span class="alias-tag rare-tag">Robin Zenith</span>
                <span class="alias-tag rare-tag">Fairy Tale Zenith</span>
                <span class="alias-tag rare-tag">Hood Zenith</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Zenith/Robin_Hood">Robin Hood</a> is one of <a href="https://browndust2.miraheze.org/wiki/Zenith">Zenith's</a> costumes. Used as Chainer and Amplifier.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- S -->
    <h2 class="letter-heading">S</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Sacred Justia</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Bustia</span>
                <span class="alias-tag">SJustia</span>
                <span class="alias-tag rare-tag">Winged Justia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sacred_Justia">Sacred Justia</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Sage of Blue Clouds Olstein</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Sage Olstein</span>
                <span class="alias-tag rare-tag">SoBC Olstein</span>
                <span class="alias-tag rare-tag">SBC Olstein</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olstein/Sage_of_Blue_Clouds">Sage of Blue Clouds</a> is one of <a href="https://browndust2.miraheze.org/wiki/Olstein">Olstein's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Scale of the Sea God</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Flat HP Armor</span>
                <span class="alias-tag rare-tag">DEF / Flat HP Armor</span>
                <span class="alias-tag rare-tag">DEF / HP Armor</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scale_of_the_Sea_God">Scale of the Sea God</a> is a UR Craftable Armor.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Scheherazade</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Schera</span>
                <span class="alias-tag">Sche</span>
                <span class="alias-tag">Schehe</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scheherazade">Scheherazade</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>School Queen Emma</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">School Emma</span>
                <span class="alias-tag rare-tag">SQ Emma</span>
                <span class="alias-tag rare-tag">Queen Emma</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Emma/School_Queen">School Queen</a> is one of <a href="https://browndust2.miraheze.org/wiki/Emma">Emma's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Selective Draw Ticket</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Purple Tix</span>
                <span class="alias-tag">Purple Tickets</span>
                <span class="alias-tag">Selective Tix</span>
                <span class="alias-tag">Selective Tickets</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Selective_Draw_Ticket">Selective Draw Ticket</a> is a Resource used to obtain Costumes or Gear from specific Banners.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Shackle of Treachery</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Shackle</span>
                <span class="alias-tag">MATK% Glove</span>
                <span class="alias-tag rare-tag">MATK% / MATK% Glove</span>
                <span class="alias-tag rare-tag">Double MATK% Glove</span>
                <span class="alias-tag rare-tag">SoT</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Shackle_of_Treachery">Shackle of Treachery</a> is a UR Craftable Glove.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Shadow Bunny Eleaneer</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Bunny Eleaneer</span>
                <span class="alias-tag rare-tag">Bunny Ele</span>
                <span class="alias-tag rare-tag">BEleaneer</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eleaneer/Shadow_Bunny">Shadow Bunny</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eleaneer">Eleaneer's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Shadowed Dream Sonya</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Sonya</span>
                <span class="alias-tag rare-tag">SD Sonya</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sonya/Shadowed_Dream">Shadowed Dream</a> is one of <a href="https://browndust2.miraheze.org/wiki/Sonya">Sonya's</a> costumes. Used as Amplifier and <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Shattered Dream Palette</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Palette</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Palette/Shattered_Dream">Shattered Dream</a> is one of <a href="https://browndust2.miraheze.org/wiki/Palette">Palette's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Shrine Maiden of Purification Granadair</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Shrine Grana</span>
                <span class="alias-tag">Shrine Granadair</span>
                <span class="alias-tag rare-tag">SMoP</span>
                <span class="alias-tag rare-tag">SMoP Grana</span>
                <span class="alias-tag rare-tag">SMoP Granadair</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granadair/Shrine_Maiden_of_Purification">Shrine Maiden of Purification</a> is one of <a href="https://browndust2.miraheze.org/wiki/Granadair">Granadair's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Stat Reduction</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Shred</span>
            </div>
            <p>Stat (<span class="cross-link" onclick="searchFor('ATK')">ATK</span>, <span class="cross-link" onclick="searchFor('MATK')">MATK</span>, <span class="cross-link" onclick="searchFor('DEF')">DEF</span>, <span class="cross-link" onclick="searchFor('MRES')">MRES</span>) reduction, mostly by some Ability.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Skill Points</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">SP</span>
            </div>
            <p>Skill Points, used to activate Costume abilities.</p>
        </li>
        <li class="slang-item" data-keywords="Slimes">
            <h3>Slime</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
            </div>
            <p>Slime is a collective term for Red, Blue, and Yellow Slimes, which are used as EXP consumables to level up Characters.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Snow White Ventana</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">SW Ventana</span>
                <span class="alias-tag rare-tag">SW Vent</span>
                <span class="alias-tag rare-tag">Snow Ventana</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ventana/Snow_White">Snow White</a> is one of <a href="https://browndust2.miraheze.org/wiki/Ventana">Ventana's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Solar Brilliance</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Flat HP Helm</span>
                <span class="alias-tag rare-tag">MRES / Flat HP Helm</span>
                <span class="alias-tag rare-tag">MRES / HP Helm</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Solar_Brilliance">Solar Brilliance</a> is a UR Craftable Helmet.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Sonya</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Tanya</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sonya">Sonya</a> is a playable Darkness Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>SP Generation</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">SP Gen</span>
            </div>
            <p>Process of recovering <span class="cross-link" onclick="searchFor('SP)">SP</span> to the team by a specific costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>SP Generator</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">SP Battery</span>
                <span class="alias-tag">Battery</span>
                <span class="alias-tag rare-tag">SP Gen</span>
            </div>
            <p>SP Generator is a costume that recovers <span class="cross-link" onclick="searchFor('SP)">SP</span> to the team.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Spark of Rampage</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Spark</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Spark_of_Rampage">Spark of Rampage</a> is a Resource used to upgrade the <a href="https://botan14xd.github.io/BD2-Overview/character-progression/burst/">Burst</a> of Costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Staller</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
            </div>
            <p>A Character or Costume whose job is to make the fight as long as possible, stalling it.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Rank-Up Stars</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Stars</span>
            </div>
            <p>Stars is a collective term for the different tiers of Rank-Up Stars (ranging from ★1 to ★4) used to increase a character's maximum level cap.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Starlight Guardian Tyr</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Tyr</span>
                <span class="alias-tag rare-tag">SG Tyr</span>
                <span class="alias-tag rare-tag">Guardian Tyr</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Tyr/Starlight_Guardian">Starlight Guardian</a> is one of <a href="https://browndust2.miraheze.org/wiki/Tyr">Tyr's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Steel Engine Rafina</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Rafina</span>
                <span class="alias-tag rare-tag">SE Raf</span>
                <span class="alias-tag rare-tag">SE Rafina</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rafina/Steel_Engine">Steel Engine</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rafina">Rafina's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Story Pack</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">Story</span>
                <span class="alias-tag">Chapter</span>
                <span class="alias-tag">Ch</span>
                <span class="alias-tag rare-tag">SP</span>
            </div>
            <p>Story Packs are a specific pack type, set in an original universe of the main story.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Stray Cat Rou</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">SC Rou</span>
                <span class="alias-tag rare-tag">Half Anni Rou</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rou/Stray_Cat">Stray Cat</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rou">Rou's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Summer Vacation Dalvi</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Summer Dalvi</span>
                <span class="alias-tag rare-tag">SV Dalvi</span>
                <span class="alias-tag rare-tag">Beach Dalvi</span>
                <span class="alias-tag rare-tag">Bikini Dalvi</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Dalvi/Summer_Vacation">Summer Vacation</a> is one of <a href="https://browndust2.miraheze.org/wiki/Dalvi">Dalvi's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Sword Breaker Alec</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">SB Alec</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Alec/Sword_Breaker">Sword Breaker</a> is one of <a href="https://browndust2.miraheze.org/wiki/Alec">Alec's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Sword Maiden</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">SM</span>
                <span class="alias-tag">Maiden</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sword_Maiden">Sword Maiden</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Sylvia</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Sylv</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sylvia">Sylvia</a> is a playable Water Character.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- T -->
    <h2 class="letter-heading">T</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Taros Tactical Manual</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">TTM</span>
                <span class="alias-tag">Tac Manual</span>
                <span class="alias-tag">Taros Manual</span>
            </div>
            <p>Taros Tactical Manual is a content focusing on completing battles created as a puzzles.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Tear of Goddess</h3>
            <div class="alias-container">
                <span class="alias-tag resource-tag ignore-exact">Resource</span>
                <span class="alias-tag">Tear</span>
                <span class="alias-tag">ToG</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Tear_of_Goddess">Tear of Goddess</a> is a Resource used to upgrade <a href="https://botan14xd.github.io/BD2-Overview/character-progression/potential-liberation/">Potential Liberation</a> of a Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Teresse</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Teres</span>
                <span class="alias-tag">Tere</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Teresse">Teresse</a> is a playable Water Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Curse Celia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Celia</span>
                <span class="alias-tag rare-tag">TC Celia</span>
                <span class="alias-tag rare-tag">CCelia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Celia/The_Curse">The Curse</a> is one of <a href="https://browndust2.miraheze.org/wiki/Celia">Celia's</a> costumes. Used as Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Destruction Alec</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">TD Alec</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Alec/The_Destruction">The Destruction</a> is one of <a href="https://browndust2.miraheze.org/wiki/Alec">Alec's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Dimension Witch Eclipse</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Eclipse</span>
                <span class="alias-tag rare-tag">DW Eclipse</span>
                <span class="alias-tag rare-tag">TDW Eclipse</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eclipse/The_Dimension_Witch">The Dimension Witch</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eclipse">Eclipse's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Empress of the Ocean Rubia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Pirate Rubia</span>
                <span class="alias-tag">Empress Rubia</span>
                <span class="alias-tag rare-tag">EO Rubia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rubia/Empress_of_the_Ocean">Empress of the Ocean</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rubia">Rubia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DEF')">DEF</span> Shredder and Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Fallen Angelica</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Ange</span>
                <span class="alias-tag">Base Angelica</span>
                <span class="alias-tag rare-tag">FAngelica</span>
                <span class="alias-tag rare-tag">TF Angelica</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Angelica/The_Fallen">The Fallen</a> is one of <a href="https://browndust2.miraheze.org/wiki/Angelica">Angelica's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Fiend Scholar Olstein</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Olstein</span>
                <span class="alias-tag rare-tag">Scholar Olstein</span>
                <span class="alias-tag rare-tag">FS Olstein</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Olstein/The_Fiend_Scholar">The Fiend Scholar</a> is one of <a href="https://browndust2.miraheze.org/wiki/Olstein">Olstein's</a> costumes. Used as <span class="cross-link" onclick="searchFor('SP Battery')">SP Battery</span> and Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Gluttonous Refithea</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Refi</span>
                <span class="alias-tag">Base Refithea</span>
                <span class="alias-tag rare-tag">TG Refi</span>
                <span class="alias-tag rare-tag">TG Refithea</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Refithea/The_Gluttonous">The Gluttonous</a> is one of <a href="https://browndust2.miraheze.org/wiki/Refithea">Refithea's</a> costumes. Used as Buffer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Lapis Witch Scheherazade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">LW Scheherazade</span>
                <span class="alias-tag">LW Schera</span>
                <span class="alias-tag">Base Schera</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scheherazade/The_Lapis_Witch">The Lapis Witch</a> is one of <a href="https://browndust2.miraheze.org/wiki/Scheherazade">Scheherazade's</a> costumes. Primarily used as a Dispel costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Magic School Professor Scheherazade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Prof Schera</span>
                <span class="alias-tag">Professor Schera</span>
                <span class="alias-tag rare-tag">MSP Schera</span>
                <span class="alias-tag rare-tag">Prof Scheherazade</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scheherazade/Magic_School_Professor">Magic School Professor</a> is one of <a href="https://browndust2.miraheze.org/wiki/Scheherazade">Scheherazade's</a> costumes. Used as Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Sharpshooter of the Mist Gray</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Gray</span>
                <span class="alias-tag rare-tag">Sharpshooter Gray</span>
                <span class="alias-tag rare-tag">Mist Gray</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Gray/The_Sharpshooter_of_the_Mist">The Sharpshooter of the Mist</a> is one of <a href="https://browndust2.miraheze.org/wiki/Gray">Gray's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Sword Queen Sylvia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">TSQ Sylvia</span>
                <span class="alias-tag">SQ Sylvia</span>
                <span class="alias-tag rare-tag">SQ Sylv</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Sylvia/The_Sword_Queen">The Sword Queen</a> is one of <a href="https://browndust2.miraheze.org/wiki/Sylvia">Sylvia's</a> costumes. Used as Self-Buffer and <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>The Void Granhildr</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Gran</span>
                <span class="alias-tag">Base Granhildr</span>
                <span class="alias-tag rare-tag">TV Granhildr</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Granhildr/The_Void">The Void</a> is one of <a href="https://browndust2.miraheze.org/wiki/Granhildr">Granhildr's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">PvP</span> Tank.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Thorn of the Desert Rubia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Rubia</span>
                <span class="alias-tag rare-tag">Thorn Rubia</span>
                <span class="alias-tag rare-tag">Desert Rubia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rubia/Thorn_of_the_Desert">Thorn of the Desert</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rubia">Rubia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DoT')">DoT</span> <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Top Idol Helena</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Helena</span>
                <span class="alias-tag rare-tag">TI Helena</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Helena/Top_Idol">Top Idol</a> is one of <a href="https://browndust2.miraheze.org/wiki/Helena">Helena's</a> costumes. Used as Support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Tower of Desire</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">ToD</span>
                <span class="alias-tag">Desire</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle#tower-of-desire">Tower of Desire</a> is one of the towers inside the <a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle">Evil Castle</a>, offering one-time clear content.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Tower of Jealousy</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">ToJ</span>
                <span class="alias-tag">Jealousy</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle#tower-of-jealousy">Tower of Jealousy</a> is one of the towers inside the <a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle">Evil Castle</a>, offering one-time clear content.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Tower of Pride</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">ToP</span>
                <span class="alias-tag">Pride</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle#tower-of-pride">Tower of Pride</a> is one of the towers inside the <a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle">Evil Castle</a>, offering one-time clear content.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Tower of Salvation</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">ToS</span>
                <span class="alias-tag">Salvation</span>
                <span class="alias-tag">Roguelike</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle#tower-of-salvation">Tower of Salvation</a> is one of the towers inside the <a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle">Evil Castle</a>, offering repetitive rogue-like content.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Tower of Wrath</h3>
            <div class="alias-container">
                <span class="alias-tag content-tag ignore-exact">Content</span>
                <span class="alias-tag">ToW</span>
                <span class="alias-tag">Wrath</span>
            </div>
            <p><a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle#tower-of-wrath">Tower of Wrath</a> is one of the towers inside the <a href="https://botan14xd.github.io/BD2-Overview/content-packs/evil-castle">Evil Castle</a>, offering one-time clear content.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Track and Field Captain Levia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">TnF Levia</span>
                <span class="alias-tag">Track Levia</span>
                <span class="alias-tag rare-tag">Sport Levia</span>
                <span class="alias-tag rare-tag">Field Levia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Levia/Track_and_Field_Captain">Track and Field Captain</a> is one of <a href="https://browndust2.miraheze.org/wiki/Levia">Levia's</a> costumes. Used as Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Track and Field Team Loen</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Track Loen</span>
                <span class="alias-tag">TnF Loen</span>
                <span class="alias-tag">Sports Loen</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Loen/Track_and_Field_Team">Track and Field Team</a> is one of <a href="https://browndust2.miraheze.org/wiki/Loen">Loen's</a> costumes. Used as Self-Buff Costume and <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Travel God's Friend</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Staff</span>
                <span class="alias-tag">MATK/CDMG Weapon</span>
                <span class="alias-tag rare-tag">CDMG Staff</span>
                <span class="alias-tag rare-tag">TGF</span>
                <span class="alias-tag rare-tag">UR Staff</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Travel_God's_Friend">Travel God's Friend</a> is a UR Craftable Weapon.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- U -->
    <h2 class="letter-heading">U</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Undefeated Glory</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">Flat HP Helm</span>
                <span class="alias-tag rare-tag">DEF / Flat HP Helm</span>
                <span class="alias-tag rare-tag">DEF / HP Helm</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Undefeated_Glory">Undefeated Glory</a> is a UR Craftable Helmet.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- V -->
    <h2 class="letter-heading">V</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Vanguard Gray</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag rare-tag">Van Gray</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Gray/Vanguard">Vanguard</a> is one of <a href="https://browndust2.miraheze.org/wiki/Gray">Gray's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Vault</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Skip</span>
            </div>
            <p>Vault is one of two possible targetting options for a Character. It targets a second Character in a Column if possible.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Venomous Touch</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag">VT</span>
                <span class="alias-tag">CDMG / CDMG Ring</span>
                <span class="alias-tag rare-tag">Double CDMG Accessory</span>
                <span class="alias-tag rare-tag">CDMG / CDMG Necklace</span>
                <span class="alias-tag rare-tag">Venom Touch</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Venomous_Touch">Venomous Touch</a> is a UR Craftable Accessory.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Very Front</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag rare-tag">VF</span>
            </div>
            <p>Very Front is one of two possible targetting options for a Character. It targets a First Character in a Column.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Violent Student Kry</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">School Kry</span>
                <span class="alias-tag rare-tag">VS Kry</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Kry/Violent_Student">Violent Student</a> is one of <a href="https://browndust2.miraheze.org/wiki/Kry">Kry's</a> costumes. Used as Knockback Costume.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Venaka</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag rare-tag">Vena</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Venaka">Venaka</a> is a playable Wind Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Ventana</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Vent</span>
                <span class="alias-tag rare-tag">Tanya</span>
                <span class="alias-tag rare-tag">Vena</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Ventana">Ventana</a> is a playable Light Character.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Vulnerability</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
                <span class="alias-tag">Vuln</span>
                <span class="alias-tag">Amp</span>
            </div>
            <p>Vulnerability is a debuff that increases incoming damage.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- W -->
    <h2 class="letter-heading">W</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Warmth of the Brazier</h3>
            <div class="alias-container">
                <span class="alias-tag gear-tag ignore-exact">Gear</span>
                <span class="alias-tag rare-tag">CRate Accessory</span>
                <span class="alias-tag rare-tag">CR / CR Necklace</span>
                <span class="alias-tag rare-tag">CRate Necklace</span>
                <span class="alias-tag rare-tag">Double CR Necklace</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Warmth_of_the_Brazier">Warmth of the Brazier</a> is a UR Craftable Accessory.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Water Park Queen Wilhelmina</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Summer Wilhelmina</span>
                <span class="alias-tag rare-tag">WPQ Wilhelmina</span>
                <span class="alias-tag rare-tag">WP Wilhelmina</span>
                <span class="alias-tag rare-tag">WPQ Wilh</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Wilhelmina/Water_Park_Queen">Water Park Queen</a> is one of <a href="https://browndust2.miraheze.org/wiki/Wilhelmina">Wilhelmina's</a> costumes. Used as Chainer.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Weak Point</h3>
            <div class="alias-container">
                <span class="alias-tag game-tag ignore-exact">Game Mechanics</span>
            </div>
            <p>Weak Point is a Boss Tile in Fiend Hunter and Guild Raid that recieves increased damage.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>White Cat Rou</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Base Rou</span>
                <span class="alias-tag rare-tag">WC Rou</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Rou/White_Cat">White Cat</a> is one of <a href="https://browndust2.miraheze.org/wiki/Rou">Rou's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>White Reaper Justia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">WR Justia</span>
                <span class="alias-tag">Base Justia</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Justia/White_Reaper">White Reaper</a> is one of <a href="https://browndust2.miraheze.org/wiki/Justia">Justia's</a> costumes. Used as <span class="cross-link" onclick="searchFor('PvP')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Whitebolt Yuri</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">WB Yuri</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Yuri/Whitebolt">Whitebolt</a> is one of <a href="https://browndust2.miraheze.org/wiki/Yuri">Yuri's</a> costumes.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Wild Dog Luvencia</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">WD Luvencia</span>
                <span class="alias-tag rare-tag">WD Luven</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Luvencia/Wild_Dog">Wild Dog</a> is one of <a href="https://browndust2.miraheze.org/wiki/Luvencia">Luvencia's</a> costumes. Used as Chainer and <span class="cross-link" onclick="searchFor('DPS')">DPS</span>.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Wind Dancer Venaka</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">WD Venaka</span>
                <span class="alias-tag">Dancer Venaka</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Venaka/Wind_Dancer">Wind Dancer</a> is one of <a href="https://browndust2.miraheze.org/wiki/Venaka">Venaka's</a> costumes. Used as Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Wilhelmina</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Wilh</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Wilhelmina">Wilhelmina</a> is a playable Water Character.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- X -->
    <h2 class="letter-heading">X</h2>
    <ul class="slang-list">
    </ul>
</div>

<div class="alpha-group"> <!-- Y -->
    <h2 class="letter-heading">Y</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Young Lady Blade</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Young Blade</span>
                <span class="alias-tag">YBlade</span>
                <span class="alias-tag">YL Blade</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Blade/Young_Lady">Young Lady</a> is one of <a href="https://browndust2.miraheze.org/wiki/Blade">Blade's</a> costumes. Used as <span class="cross-link" onclick="searchFor('DPS')">DPS</span> and Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Your Very Own Cat Eris</h3>
            <div class="alias-container">
                <span class="alias-tag costume-tag ignore-exact">Costume</span>
                <span class="alias-tag">Cat Eris</span>
                <span class="alias-tag rare-tag">YVOC Eris</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Eris/Your_Very_Own_Cat">Your Very Own Cat</a> is one of <a href="https://browndust2.miraheze.org/wiki/Eris">Eris's</a> costumes. Used as Amplifier.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Yozakura</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Yoza</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Yozakura">Yozakura</a> is a playable Wind Character.</p>
        </li>
    </ul>
</div>

<div class="alpha-group"> <!-- Z -->
    <h2 class="letter-heading">Z</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Zenith</h3>
            <div class="alias-container">
                <span class="alias-tag character-tag ignore-exact">Character</span>
                <span class="alias-tag">Zen</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Zenith">Zenith</a> is a playable Wind Character.</p>
        </li>
    </ul>
</div>

<script>
let searchTimeout = null;
let activeCategory = "";

function toggleCategory(category) {
    if (activeCategory === category) {
        activeCategory = "";
    } else {
        activeCategory = category;
    }

    let buttons = document.querySelectorAll('.quick-filters button');
    buttons.forEach(btn => btn.classList.remove('active-filter'));

    if (activeCategory !== "") {
        let safeId = 'btn-' + activeCategory.replace(/\s+/g, '-'); 
        let activeBtn = document.getElementById(safeId);
        if (activeBtn) activeBtn.classList.add('active-filter');
    }

    filterSlang();
}

function searchFor(term) {
    let searchInput = document.getElementById("slangSearch");
    searchInput.value = term;
    activeCategory = "";
    let buttons = document.querySelectorAll('.quick-filters button');
    buttons.forEach(btn => btn.classList.remove('active-filter'));
    filterSlang();
    searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function filterSlang() {
    if (searchTimeout) {
        clearTimeout(searchTimeout);
    }

    searchTimeout = setTimeout(function() {
        const cleanText = (str) => {
            if (!str) return "";
            return str.replace(/-/g, ' ').toUpperCase().replace(/\s+/g, ' ').trim();
        };

        let rawInput = document.getElementById("slangSearch").value;
        let inputText = cleanText(rawInput);
        let categoryInput = cleanText(activeCategory); 
        
        let groups = document.getElementsByClassName("alpha-group");
        let totalVisible = 0; 

        for (let i = 0; i < groups.length; i++) {
            let items = groups[i].getElementsByClassName("slang-item");
            let visibleCount = 0;

            for (let j = 0; j < items.length; j++) {
                let item = items[j];
                
                let title = item.querySelector('h3');
                let titleText = title ? cleanText(title.textContent) : "";
                
                let tags = item.querySelectorAll('.alias-tag, .tag-rare, .rare-tag, [class*="tag-"]');
                let tagsText = "";
                let itemHasCategory = false; 
                
                let ignoredCategories = ["CHARACTER", "COSTUME", "CONTENT", "GAME MECHANICS", "GEAR", "RESOURCE"];

                for (let k = 0; k < tags.length; k++) {
                    let singleTagText = cleanText(tags[k].textContent);

                    if (categoryInput !== "" && singleTagText === categoryInput) {
                        itemHasCategory = true;
                    }

                    if (!ignoredCategories.includes(singleTagText)) {
                        tagsText += singleTagText + " ";
                    }
                }
                let hiddenKeywords = item.getAttribute("data-keywords");
                let keywordsText = hiddenKeywords ? cleanText(hiddenKeywords) : "";
                let searchableText = titleText + " " + tagsText + " " + keywordsText;

                let passesText = false;
                if (inputText === "") {
                    passesText = true;
                } else if (inputText.length <= 2) {
                    let regex = new RegExp("\\b" + inputText + "\\b");
                    passesText = regex.test(searchableText);
                } else {
                    passesText = (searchableText.indexOf(inputText) > -1);
                }
                let passesCategory = (categoryInput === "" || itemHasCategory);

                if (passesText && passesCategory) {
                    item.style.display = "";
                    visibleCount++;
                    totalVisible++; 

                    let isExact = false;
                    if (inputText !== "") {
                        if (titleText === inputText) isExact = true;
                        if (keywordsText.indexOf(inputText) > -1) {
                            let keywordsArray = keywordsText.split(" ");
                            if (keywordsArray.includes(inputText)) isExact = true;
                        }
                        
                        for (let k = 0; k < tags.length; k++) {
                            if (tags[k].classList.contains("ignore-exact")) continue; 
                            if (cleanText(tags[k].textContent) === inputText) isExact = true;
                        }
                    }

                    if (isExact) {
                        if (!item.classList.contains("exact-match")) item.classList.add("exact-match");
                    } else {
                        if (item.classList.contains("exact-match")) item.classList.remove("exact-match");
                    }

                } else {
                    item.style.display = "none";
                    if (item.classList.contains("exact-match")) item.classList.remove("exact-match");
                }
            }

            if (visibleCount === 0) {
                groups[i].style.display = "none";
            } else {
                groups[i].style.display = "";
            }
        }
        
        let counterDiv = document.getElementById("slang-counter");
        if (counterDiv) {
            let word = (totalVisible === 1) ? "term" : "terms";

            if (totalVisible === 0) {
                counterDiv.textContent = "No terms found";
            } else if (inputText === "" && categoryInput === "") {
                counterDiv.textContent = "Showing all " + totalVisible + " " + word;
            } else {
                counterDiv.textContent = "Found " + totalVisible + " " + word;
            }
        }
        
    }, 250); 
}

document.addEventListener("DOMContentLoaded", filterSlang);
</script>

<style>
.md-typeset a[target="_blank"]::after,
.md-typeset a[href^="http://"]::after,
.md-typeset a[href^="https://"]::after {
    display: none !important;
}
</style>