<input type="text" id="slangSearch" onkeyup="filterSlang()" placeholder="Search for slang or characters..." class="slang-search-box">

<div class="alpha-group">
    <h2 class="letter-heading">D</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="poison burn bleed">
            <h3>Damage over Time</h3>
            <div class="alias-container">
                <span class="alias-tag">DoT</span>
            </div>
            <p>Effects that deal damage at the end of a turn.</p>
        </li>
    </ul>
</div>

<div class="alpha-group">
    <h2 class="letter-heading">S</h2>
    <ul class="slang-list">
        <li class="slang-item" data-keywords="battery">
            <h3>SP Gen</h3>
            <p>A costume or character designed primarily to generate Skill Points.</p>
        </li>
        <li class="slang-item">
            <h3>Shrine Maiden of Purification Granadair</h3>
            <div class="alias-container">
                <span class="alias-tag">SMoP</span>
            </div>
            <p>High-tier buffer.</p>
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