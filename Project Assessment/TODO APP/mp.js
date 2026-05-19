// // Store Data in Array
// let tasks = [];

// // Add Task
// function addTask(taskName){

//   tasks.push({
//     text: taskName,
//     completed: false
//   });

//   console.log(tasks);
// }

// // Example
// addTask("HTML");
// addTask("CSS");
// addTask("JavaScript");



// // CRUD - Edit
// function editTask(index){

//   const updatedTask = prompt("Edit Task", tasks[index].text);

//   // Validation
//   if(updatedTask === null || updatedTask.trim() === ""){
//     return;
//   }

//   tasks[index].text = updatedTask.trim();

//   renderTasks();
// }



li.innerHTML = `
  <span>${task.text}</span>

  <div class="actions">

    <button class="complete-btn" onclick="toggleTask(${index})">
      ${task.completed ? "Undo" : "Done"}
    </button>

    <button class="edit-btn" onclick="editTask(${index})">
      Edit
    </button>

    <button class="delete-btn" onclick="deleteTask(${index})">
      Delete
    </button>

  </div>
`;

// Edit Task
function editTask(index){

  const updatedTask = prompt(
    "Edit Task",
    tasks[index].text
  );

  // Validation
  if(updatedTask === null || updatedTask.trim() === ""){
    return;
  }

  // Update Task
  tasks[index].text = updatedTask.trim();

  // Save Local Storage
  localStorage.setItem("tasks", JSON.stringify(tasks));

  // Re-render
  renderTasks();
}
