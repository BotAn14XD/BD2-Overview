<input type="text" id="slangSearch" onkeyup="filterSlang()" placeholder="Search for slang or characters..." class="slang-search-box">

<div class="alpha-group">
    <h2 class="letter-heading">M</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Mamonir</h3>
            <div class="alias-container">
                <span class="alias-tag">Mamo</span>
                <span class="character-tag">Character</span>
            </div>
            <p>Mamonir, one of playable Characters.</p>
        </li>
    </ul>
</div>

<div class="alpha-group">
    <h2 class="letter-heading">N</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Might of Death Mamonir</h3>
            <div class="alias-container">
                <span class="alias-tag">NoD Mamo</span>
                <span class="alias-tag">Base Mamo</span>
                <span class="alias-tag">Base Mamonir</span>
                <span class="costume-tag">Costume</span>
            </div>
            <p>One of Mamonir costumes. Chainer and DPS.</p>
        </li>
    </ul>
</div>

<div class="alpha-group">
    <h2 class="letter-heading">S</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="">
            <h3>Scheherazade</h3>
            <div class="alias-container">
                <span class="alias-tag">Schera</span>
                <span class="character-tag">Character</span>
            </div>
            <p><a href="https://browndust2.miraheze.org/wiki/Scheherazade">Scheherazade</a>, one of playable Characters.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Shrine Maiden of Purification Granadair</h3>
            <div class="alias-container">
                <span class="alias-tag">SMoP</span>
                <span class="alias-tag">SMoP Grana</span>
                <span class="alias-tag">SMoP Gradanair</span>
                <span class="alias-tag">Shrine Grana</span>
                <span class="alias-tag">Shrine Granadair</span>
                <span class="costume-tag">Costume</span>
            </div>
            <p>One of Granadair costumes. Meta support.</p>
        </li>
        <li class="slang-item" data-keywords="">
            <h3>Skill Points</h3>
            <div class="alias-container">
                <span class="alias-tag">SP</span>
                <span class="game-tag">Game Mechanics</span>
            </div>
            <p>One of Granadair costumes. Meta support.</p>
        </li>
    </ul>
</div>

<script>
function filterSlang() {
    let input = document.getElementById("slangSearch").value.toUpperCase();

    let groups = document.getElementsByClassName("alpha-group");

    for (let i = 0; i < groups.length; i++) {
        let items = groups[i].getElementsByClassName("slang-item");
        let visibleCount = 0;

        for (let j = 0; j < items.length; j++) {
            let visibleText = items[j].innerText.toUpperCase();
            let hiddenKeywords = (items[j].getAttribute("data-keywords") || "").toUpperCase();
            
            if (visibleText.indexOf(input) > -1 || hiddenKeywords.indexOf(input) > -1) {
                items[j].style.display = "";
                visibleCount++; // Found one!
            } else {
                items[j].style.display = "none";
            }
        }

        if (visibleCount === 0) {
            groups[i].style.display = "none";
        } else {
            groups[i].style.display = "";
        }
    }
}
</script>