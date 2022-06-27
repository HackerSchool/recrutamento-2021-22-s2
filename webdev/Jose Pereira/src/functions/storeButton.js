import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
/* Creates a store button */
function renderStoreButton() {
  const buttonContainer = createHTMLelement("div", "btnContainer", "", "");
  const button = createHTMLelement(
    "a",
    "storebutton",
    "",
    "VIEW ALL PRODUCTS"
  );
  button.href = "https://bakerskateboards.com/collections/holiday-21";
  buttonContainer.appendChild(button);
  /* Append to the DOM */
  maindiv.appendChild(buttonContainer);
}

export { renderStoreButton };
