const element = document.querySelector("#volunteerKinds");

function createInput() {
  const element = document.querySelector("#volunteerKinds");
  console.log(element.value);

  if (element.value === "플로깅") {
    const firstPlace = document.querySelector(".firstPlace");
    const newInput = document.createElement("input");
    newInput.type = "text";
    newInput.name = "place";
    firstPlace.appendChild(newInput);
  }
}
element.addEventListener(onclick, createInput);
