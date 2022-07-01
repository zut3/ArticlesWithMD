const converter = new showdown.Converter();

const convertToHtml = (from, to) => {
    to.innerHTML = converter.makeHtml(from)
}

const onInput = (e) => {
    const text = e.target.value;
    const target = document.getElementById("preview")
    convertToHtml(text, target)
}


const mdArea = document.getElementById("md-text");

convertToHtml(mdArea.value,  document.getElementById("preview"))

mdArea.oninput = onInput
