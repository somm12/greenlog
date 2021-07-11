function handleOnChange(e) {
  const value = e.value;
  const formInput = Document.querySelector(form);
  
  console.log(formInput);
  if (value === "플로깅") {
    const firstPlace = document.querySelector(".firstPlace");
    const newDiv = document.createElement("span");
    newDiv.innerHTML = "플로깅 첫 시작 장소 ";

    const newInput = document.createElement("input");
    newInput.type = "text";
    newInput.name = "place";

    firstPlace.appendChild(newDiv);
    firstPlace.appendChild(newInput);
  } else {
    const e1 = document.querySelector(".firstPlace span");
    const e2 = document.querySelector(".firstPlace input");

    if (e1 !== null && e2 !== null) {
      e1.remove();
      e2.remove();
    }
  }
}
