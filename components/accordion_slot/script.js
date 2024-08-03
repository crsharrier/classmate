const accordionHeaderButtons = document.querySelectorAll('.accordion-header-button'); // Target parent divs of buttons

accordionHeaderButtons.forEach(header => {
  header.addEventListener('click', function(event) {

        const accordionBody = document.querySelector(`${header.dataset.accordionTarget}`)
        const buttonsContainer = header.querySelector('.accordion-buttons-container')
            
        if (accordionBody.classList.contains('hidden')) {
            // Accordion is opening
            // Hide buttons in other accordions
            const otherButtonsContainers = document.querySelectorAll('.accordion-buttons-container:not(.hidden)');
            otherButtonsContainers.forEach(container => {
                container.classList.add('hidden');
            })

            buttonsContainer.classList.remove('hidden');
            
        } else {
            // Accordion is closing
            buttonsContainer.classList.add('hidden');

            const listItems = document.querySelectorAll('.cm-list-item');
            listItems.forEach(listItem => {
                hideListItemButtons(listItem)
            });
            
        }

  });

});


const addButtons = document.querySelectorAll('.lists-add-button');
const editButtons = document.querySelectorAll('.lists-edit-button');

addButtons.forEach(addButton => {
    addButton.addEventListener('click', (event) => {
      // Your logic for handling the "add" button click
      event.stopPropagation();
    });
  });
  
  editButtons.forEach(editButton => {
    editButton.addEventListener('click', (event) => {
      // Your logic for handling the "edit" button click
      event.stopPropagation();
    });
  });
  