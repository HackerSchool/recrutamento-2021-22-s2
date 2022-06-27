import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
import Item1 from "../img/item1.png";
import Item2 from "../img/item2.png";
import Item3 from "../img/item3.png";
import Item4 from "../img/item4.png";
import Item5 from "../img/item5.png";
import Item6 from "../img/item6.png";
import Item7 from "../img/item7.png";
import Item8 from "../img/item8.png";
import Item9 from "../img/item9.png";
import Item10 from "../img/item10.png";
import Item11 from "../img/item11.png";
import Item12 from "../img/item12.png";

/* Creates a store */
function renderStore() {
  /* store container element */
  const store = createHTMLelement("div", "store", "", "");

  /* items images */
  const items = [
    Item1,
    Item2,
    Item3,
    Item4,
    Item5,
    Item6,
    Item7,
    Item8,
    Item9,
    Item10,
    Item11,
    Item12,
  ];

  /* items texts */
  const text = [
    "Kader Logo Navy B2 8.25",
    "Theotis Logo Mandarin B2 8.0",
    "Spanky Logo Forest B2 8.5",
    "Circle Jerks Album Art Deck 9.6",
    "Circle Jerks Tee White",
    "Capital B Stripe Tee Green/Yellow",
    "Kamikaze Tee Black",
    "Domination Tee Black",
    "Times New Black Snapback",
    "Jolly Man Red Socks",
    "Misty Flip Sticker",
    "Circle Jerks Sticker",
  ];

  /* items prices */
  const price = [
    "$ 71",
    "$ 71",
    "$ 73",
    "$ 75",
    "$ 35",
    "$ 40",
    "$ 35",
    "$ 35",
    "$ 40",
    "$ 12",
    "$ 2",
    "$ 2",
  ];

  const links = [
    "https://bakerskateboards.com/collections/holiday-21/products/kader-logo-navy-b2-8-25",
    "https://bakerskateboards.com/collections/holiday-21/products/theotis-logo-mandarin-b2-8-0",
    "https://bakerskateboards.com/collections/holiday-21/products/spanky-logo-forest-b2-8-5",
    "https://bakerskateboards.com/collections/holiday-21/products/circle-jerks-album-art-deck-9-6",
    "https://bakerskateboards.com/collections/holiday-21/products/circle-jerks-tee-white",
    "https://bakerskateboards.com/collections/holiday-21/products/capital-b-stripe-tee-green-yellow",
    "https://bakerskateboards.com/collections/holiday-21/products/kamikaze-tee-black",
    "https://bakerskateboards.com/collections/holiday-21/products/domination-tee-black",
    "https://bakerskateboards.com/collections/holiday-21/products/times-new-black-snapback",
    "https://bakerskateboards.com/collections/holiday-21/products/jolly-man-red-socks",
    "https://bakerskateboards.com/collections/holiday-21/products/misty-flip-sticker",
    "https://bakerskateboards.com/collections/holiday-21/products/circle-jerks-sticker",
  ];

  let i = 0;
  items.forEach((item) => {
    const placeholder = createHTMLelement("a", "", ["placeholder"], "");
    placeholder.href = links[i]
    /* image */
    const placeholder_img = createHTMLelement("img", "", ["skate_img"], "");
    placeholder_img.src = item;
    placeholder.appendChild(placeholder_img);

    /* text */
    const placeholder_txt = createHTMLelement("p", "", ["skate_txt"], text[i]);
    placeholder.appendChild(placeholder_txt);

    /* price */
    const placeholder_price = createHTMLelement(
      "p",
      "",
      ["skate_price"],
      price[i]
    );
    placeholder.appendChild(placeholder_price);

    store.appendChild(placeholder);
    i++;
  });
  /* Append to the DOM */
  maindiv.appendChild(store);
}

export { renderStore };
