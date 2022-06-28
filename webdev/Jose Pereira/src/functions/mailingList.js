import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
/* Creates a mailing list section */
function renderMailingList() {
  const formDiv = createHTMLelement("div", "formDiv", "", "")
  /* Mailing list form */
  const form = createHTMLelement("form", "mail", "", "");
  const label = createHTMLelement("label", "", "", "join our mailing list");
  /* input (default type = text) box */
  const inputBox = createHTMLelement("div", "", "", "");
  const input = createHTMLelement("input", "", "", "");
  input.placeholder = "Enter your email address";
  /* placeholder */
  const buttonBox = createHTMLelement("div", "", "", "");
  const button = createHTMLelement("button", "mailBtn", "", "subscribe");

  /* Add everything */
  inputBox.appendChild(input);
  buttonBox.appendChild(button);
  form.appendChild(label);
  form.appendChild(inputBox);
  form.appendChild(buttonBox);
  formDiv.appendChild(form)
  /* Append to the DOM */
  maindiv.appendChild(formDiv);
}

export { renderMailingList };
