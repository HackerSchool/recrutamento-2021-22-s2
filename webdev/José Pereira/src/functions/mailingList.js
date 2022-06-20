import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
/* Creates a mailing list section */
function renderMailingList() {
  const test = createHTMLelement("div", "", "", "")
  /* Append to the DOM */
  maindiv.appendChild(test);
}

export { renderMailingList };
