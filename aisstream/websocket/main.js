import { createBoard, playMove } from "./connect4.js";

window.addEventListener("DOMContentLoaded", () => {
    // initialize the UI
    const board = document.querySelector(".board");
    createBoard(board);
})