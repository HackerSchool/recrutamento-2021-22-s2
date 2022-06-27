import { renderAnnouncementBar } from "./functions/announcementBar";
import { renderNav } from "./functions/navbar";
import { renderSpacer } from "./functions/spacer";
import { renderStore } from "./functions/store";
import { renderStoreButton } from "./functions/storeButton";
import { renderMailingList } from "./functions/mailingList";
import { renderFooter } from "./functions/footer";

/*           GitHub pages deployment link          */
/* https://pearsettings44.github.io/Baker-Clone-HS/ */


/* Main div, contains everything */
const maindiv = document.getElementById("content");
renderAnnouncementBar();
renderNav();
renderSpacer();
renderStore();
renderStoreButton();
renderMailingList();
renderFooter();
export { maindiv };
