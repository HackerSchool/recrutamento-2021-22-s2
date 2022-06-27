import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
/* Creates a mailing list section */
function renderFooter() {
  const footer = createHTMLelement("footer", "footer", "", "");
  const brandName = createHTMLelement("a", "brand", "", "© baker skateboards");
  const shopify = createHTMLelement(
    "a",
    "shopify",
    "",
    "Shopping Cart by Shopify"
  );
  brandName.href = "#";
  shopify.target = "_blank";
  shopify.href =
    "https://www.shopify.com/tour/shopping-cart?utm_campaign=poweredby&utm_medium=shopify&utm_source=onlinestore";
  footer.appendChild(brandName);
  footer.appendChild(shopify);
  /* Append to the DOM */
  maindiv.appendChild(footer);
}

export { renderFooter };
