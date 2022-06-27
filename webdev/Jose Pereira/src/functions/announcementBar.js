import { createHTMLelement } from "./createElements";
import { maindiv } from "../index";
/* Creates an announcement bar */
function renderAnnouncementBar() {
  const content = "CLICK TO WATCH THE BAKER VIDEO WITH TYSON AND T-FUNK";
  const video = "https://www.youtube.com/watch?v=dGCopkpYuOg&t=12s";

  const header = createHTMLelement("header", "header", "", "");
  const header_content = createHTMLelement("a", "header_video", "", content);

  header_content.href = video;
  header_content.target = "_blank";
  header.appendChild(header_content);
  /* Append to the DOM */
  maindiv.appendChild(header);
}

export { renderAnnouncementBar };
