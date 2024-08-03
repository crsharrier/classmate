let modal;
let modalCloseButton;

function initModal() {
	modal = document.querySelector('.modal');
	modalCloseButton = modal.querySelector('.close-modal');

	modalCloseButton.addEventListener('click', () => {
		closeModal();
	});
}

function closeModal() {
	modal.classList.add('closing');
	modal.addEventListener('animationend', () => {
		modal.remove();
	}, { once: true });
}
