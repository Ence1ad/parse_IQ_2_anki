front_template = """<div id="items">
	<div id="path"></div>
	<div id="deck">{{Deck}}</div>
	<div id="front">
		{{Question}}
	</div>
</div>
<script>
	deck = document.getElementById("deck");
	dName = deck.innerText.split("::")
	deck.innerHTML = dName[dName.length-1];
	document.getElementById("path").innerHTML = dName.join(" > ");
	function addTitle(id=false, title="") {
		let el = document.getElementById(id);
		if (el.innerText) {
			let t = document.createElement("div");
			t.classList.add("title");
			t.innerHTML = title;

			let b = document.createElement("div");
			b.classList.add("body");
			b.innerHTML = el.innerHTML;

			while(el.firstChild) {
				el.removeChild(el.firstChild);
			}
			el.append(t, b);
		} 
	}
	addTitle("front", "");
</script>"""

back_template = """<div id="items">
	<div id="path"></div>
	<div id="deck">{{Deck}}</div>
	<div id="front">
		{{Question}}
	</div>

<div id="sound-media"><hr>play audio{{Back_Sound}}</div>
	<div id="back-basic">
		{{Back_Text}}
	</div>

	<div id="back-code">
		{{Back_Code}}
	</div>
	<div id="additional-info">{{Additional Info}}</div>
	<div id="options"></div>
	<div id="example">{{Example}}</div>
</div>
<script>
	deck = document.getElementById("deck");
	dName = deck.innerText.split("::")
	deck.innerHTML = dName[dName.length-1];
	document.getElementById("path").innerHTML = dName.join(" > ");

[...document.getElementById("items").children].map((el)=> el.innerText ? null : el.classList.add("hidden"));	

	function addTitle(id=false, title="") {
		let el = document.getElementById(id);
		if (el.innerText) {
			let t = document.createElement("div");
			t.classList.add("title");
			t.innerHTML = title;

			let b = document.createElement("div");
			b.classList.add("body");
			b.innerHTML = el.innerHTML;

			while(el.firstChild) {
				el.removeChild(el.firstChild);
			}
			el.append(t, b);
		} 
	}
	addTitle("front", "");
	addTitle("back-basic", "");
	addTitle("back-code", "");
	addTitle("options", "With Optional Params: ");
	addTitle("example", "");
	addTitle("additional-info", "&#9432;");
</script>"""