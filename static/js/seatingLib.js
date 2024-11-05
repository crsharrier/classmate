
// Variables for holding selected item
var selectedItem = null;
var dragStartPoint = null;

// Function to create a desk (rectangle)
function createDesk(position, rotation, size, color, name_1, name_2) {
    var desk = new Path.Rectangle({
        point: position,
        size: size,
        fillColor: color,
        strokeColor: '#000000',
        strokeWidth: 2,
        rotation: rotation
    });

    // Add text for the student's name on either side of the desk
    var textAbove = new PointText({
        point: [desk.bounds.leftCenter.x + 5, desk.bounds.leftCenter.y],
        content: name_1,
        fillColor: 'black',
        fontFamily: 'Arial',
        fontSize: 16,
        justification: 'left'
    });

    var textBelow = new PointText({
        point: [desk.bounds.rightCenter.x - 5, desk.bounds.rightCenter.y],
        content: name_2,
        fillColor: 'black',
        fontFamily: 'Arial',
        fontSize: 16,
        justification: 'right'
    });

    // Enable dragging
    desk.onMouseDrag = function(event) {
        if (selectedItem === this) {
            this.position += event.delta;
            textAbove.position += event.delta;
            textBelow.position += event.delta;
        }
    };

    // Enable rotation on double click
    desk.onDoubleClick = function(event) {
        if (selectedItem === this) {
            this.rotate(15);
            textAbove.rotate(15);
            textBelow.rotate(15);
        }
    };

    return desk;
}


// Function to create a desk (rectangle)
function createStudentDesk(deskData) {
    return createDesk(
        deskData.position,
        deskData.rotation,
        [160, 80],
        '#cccccc',
        deskData.student_1,
        deskData.student_2
    )
}

// Function to create a desk (rectangle)
function createTeacherDesk(position) {
    return createDesk(
        position,
        0,
        [250, 100],
        '#444444',
        "",
        ""
    )
}

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

