import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
import Menu from "../img/menu.png";
import Logo from "../img/baker.png";
import User from "../img/user.png";
import Search from "../img/search.png";
import Bag from "../img/bag.png";

/* Creates a navbar with menu, logo, currency, user, search and shopping bag */
function renderNav() {
  /* navbar element */
  const navbar = createHTMLelement("nav", "navbar");

  /* menu */
  const menu = createHTMLelement("div", "menu", "", "");
  const menu_img = createHTMLelement("img", "", "", "");
  menu_img.src = Menu;
  menu.appendChild(menu_img);
  navbar.appendChild(menu);

  /* logo */
  const logo = createHTMLelement("a", "logo", "", "");
  const logo_img = createHTMLelement("img", "", "", "");
  const videoBaker = "https://bakerskateboards.com/";
  logo_img.src = Logo;
  logo.href = videoBaker;
  logo.target = "_blank";
  logo.appendChild(logo_img);
  navbar.appendChild(logo);

  /* options */
  const options = createHTMLelement("div", "options", "", "");

  /* dropdown menu */
  const dropdown_container = createHTMLelement("div", "", "", "");
  const dropdown = createHTMLelement("select", "dropdown", "", "");
  dropdown_container.appendChild(dropdown); 
  options.appendChild(dropdown_container);

  const dropdown_options = ["USD", "CAD", "EUR", "GBP"];
  dropdown_options.forEach((currency) => {
    const dropdown_option = createHTMLelement("option", "", "", currency);
    dropdown.appendChild(dropdown_option);
  });

  /* options items (user, search, bag) */
  const items = ["user", "search", "bag"];
  const images = [User, Search, Bag];
  let i = 0;

  items.forEach((item) => {
    const list_item = createHTMLelement("div", item, "", "");
    const list_item_img = createHTMLelement("img", "", "", "");
    list_item_img.src = images[i++];
    list_item.appendChild(list_item_img);
    options.appendChild(list_item);
  });
  navbar.appendChild(options);

  /* Append to the DOM */
  maindiv.appendChild(navbar);
}

export { renderNav };
