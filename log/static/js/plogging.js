const element = document.querySelector("#volunteerKinds");

function handleOnChange(e) {
  const value = e.value;
  console.log(value);

  if (element.value === "플로깅") {
    console.log(value);
    const firstPlace = document.querySelector(".firstPlace");
    const newInput = document.createElement("input");
    newInput.type = "text";
    newInput.name = "place";
    firstPlace.appendChild(newInput);
  }
}
