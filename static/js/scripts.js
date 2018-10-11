/* JS only for detecting scroll */

let doc = document.documentElement;
let lastScrollTop = window.pageYOffset || doc.scrollTop;

window.addEventListener('scroll', () => {
	let top = window.pageYOffset || doc.scrollTop;

	if (top > lastScrollTop) {
		document.querySelector('.logo').classList.add('-on-scroll');
	}
	else {
		document.querySelector('.logo').classList.remove('-on-scroll');
	}

	lastScrollTop = top <= 0 ? 0 : top;
});