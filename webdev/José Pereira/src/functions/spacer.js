import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
/* Creates a little spacer */
function renderSpacer() {
  const spacer = createHTMLelement("div", "spacer", "", "-");
  /* Append to the DOM */
  maindiv.appendChild(spacer);
}

export { renderSpacer };
