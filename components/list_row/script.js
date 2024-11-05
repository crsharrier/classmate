const listItems = document.querySelectorAll('.cm-list-item');

function showListItemButtons(listItem) {
    const deleteButton = listItem.querySelector('.list-item-delete-button');
    const editButton = listItem.querySelector('.list-item-edit-button');
    deleteButton.classList.remove('hidden')
    editButton.classList.remove('hidden')
    listItem.classList.remove('cm-list-item');
    listItem.classList.add('cm-list-item-focus');
}

function hideListItemButtons(listItem) {
    const deleteButton = listItem.querySelector('.list-item-delete-button');
    const editButton = listItem.querySelector('.list-item-edit-button');
    deleteButton.classList.add('hidden')
    editButton.classList.add('hidden')
    listItem.classList.add('cm-list-item');
    listItem.classList.remove('cm-list-item-focus');
}

listItems.forEach(listItem => {
    listItem.addEventListener('click', () => {

        showListItemButtons(listItem)

        // Hide buttons and reapply hover effects for other items
        listItems.forEach(otherItem => {
            if (otherItem !== listItem) {
                hideListItemButtons(otherItem)
            }
        });
    });
});
