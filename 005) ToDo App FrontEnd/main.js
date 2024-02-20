var AllItems = [];

$(document).ready(function () {
    GetAllItems();
});


function GetAllItems() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:6754/GetAllItems",
        headers: {
            'Content-Type': 'application/json',
        },
        success: function (data) {
            AllItems = JSON.parse(data);
            console.log(AllItems);
            UpdateDataHTML();
        }
    });
}

function DeleteItem(id) {
    $.ajax({
        type: "DELETE",
        url: "http://127.0.0.1:6754/RemoveItem?id=" + id,
        headers: {
            'Content-Type': 'application/json',
        },
        success: function (data) {
            GetAllItems();
        }
    });
}

function UpdateItem(id, isDone) {
    let url = "";
    isDone = !isDone;
    if (isDone) { url = `http://127.0.0.1:6754/UpdateItemStatus?id=${id}&isdone=True`; }
    else { url = `http://127.0.0.1:6754/UpdateItemStatus?id=${id}&isdone=False`; }

    $.ajax({
        type: "PUT",
        url: url,
        headers: {
            'Content-Type': 'application/json',
        },
        success: function (data) {
            GetAllItems();
        }
    });
}

function AddItem(name){
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:6754/AddNewToDoItem",
        headers: {
            'Content-Type': 'application/json',
        },
        data: JSON.stringify({
            name:name
        }),
        success: function (data) {
            $("#NewItemTextBox").val("");
            GetAllItems();
        }
    });
}

function AddNewItemClicked(){
    AddItem($("#NewItemTextBox").val());
}

function GetItemLI(isDone, Name, id) {
    if (isDone) {
        return `
            <li class="list-group-item list-group-item-success">
                <div class="d-flex justify-content-between">
                    <div>${Name}</div>
                    <div>
                        <button type="button" class="btn btn-info" onclick="UpdateItem(${id}, true)"><i class="fa-solid fa-xmark"></i></button>
                        <button type="button" class="btn btn-danger" onclick="DeleteItem(${id})"><i class="fa-solid fa-trash"></i></button>
                    </div>
                </div>
            </li>
        `;
    }
    else {
        return `
        <li class="list-group-item">
        <div class="d-flex justify-content-between">
            <div>${Name}</div>
            <div>
                <button type="button" class="btn btn-info" onclick="UpdateItem(${id}, false)"><i class="fa-solid fa-check"></i></button>
                <button type="button" class="btn btn-danger" onclick="DeleteItem(${id})"><i class="fa-solid fa-trash"></i></button>
            </div>
        </div>
        </li>
    `;
    }
}

function UpdateDataHTML() {
    let fullULBody = "";
    AllItems.forEach(item => {
        fullULBody += GetItemLI(item.fields.isdone, item.fields.name, item.pk)
    });
    $("#TodoList").html(fullULBody);
}