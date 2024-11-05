
var desks = desksData.map(createStudentDesk);
var teacherDesk = createTeacherDesk([350, 500])
desks.push(teacherDesk)


// Track selection
function onMouseDown(event) {
    selectedItem = null;
    dragStartPoint = event.point;

    for (var i = 0; i < desks.length; i++) {
        if (desks[i].contains(event.point)) {
            selectedItem = desks[i];
            break;
        }
    }
}

// Deselect on mouse up
function onMouseUp(event) {
    selectedItem = null;
}

// Save layout to JSON
// document.getElementById('saveLayout').addEventListener('click', function() {
//     var layout = desks.map(function(desk) {
//         return {
//             position: desk.position,
//             rotation: desk.rotation,
//             size: desk.bounds.size
//         };
//     });

//     document.getElementById('layoutData').value = JSON.stringify(layout, null, 4);
// });

// Attach event handlers
// view.onMouseDown = onMouseDown;
// view.onMouseUp = onMouseUp;