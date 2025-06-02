$(document).ready(function() {
    function loadTodos() {
        $.get('/todos', function(data) {
            renderTodoList(data);
            updateCounters();
        });
    }

    function renderTodoList(todos) {
        const pendingList = $('#pending-list');
        const completedList = $('#completed-list');

        pendingList.empty();
        completedList.empty();

        todos.forEach(todo => {
            const li = $(`<li data-id="${todo.id}">
                <span class="${todo.completed ? 'completed' : ''}">${todo.content}</span>
                <div class="actions">
                    <button class="toggle-btn">${todo.completed ? '撤销' : '完成'}</button>
                    <button class="delete-btn">删除</button>
                </div>
            </li>`);

            (todo.completed ? completedList : pendingList).append(li);
        });
    }

    function updateCounters() {
        $('#pending-count').text($('#pending-list li').length);
        $('#completed-count').text($('#completed-list li').length);
    }

    // 添加任务
    $('#add-btn').click(function() {
        const content = $('#new-todo').val().trim();
        if (content) {
            $.ajax({
                url: '/todos',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ content: content }),
                success: function() {
                    $('#new-todo').val('');
                    loadTodos();
                }
            });
        }
    });

    // 回车添加任务
    $('#new-todo').keypress(function(e) {
        if (e.which === 13) {
            $('#add-btn').click();
        }
    });

    // 切换任务状态
    $(document).on('click', '.toggle-btn', function() {
        const $li = $(this).closest('li');
        const todoId = $li.data('id');

        $.ajax({
            url: `/todos/${todoId}/toggle`,
            type: 'PATCH',
            success: function(updatedTodo) {

                $li.find('span').toggleClass('completed');
                $li.find('.toggle-btn').text(updatedTodo.completed ? '撤销' : '完成');


                const targetList = updatedTodo.completed ?
                    $('#completed-list') :
                    $('#pending-list');

                $li.appendTo(targetList);
                updateCounters();
            }
        });
    });


    $(document).on('click', '.delete-btn', function() {
        const $li = $(this).closest('li');
        const todoId = $li.data('id');

        if (confirm('确定要删除吗？')) {
            $.ajax({
                url: `/todos/${todoId}`,
                type: 'DELETE',
                success: function() {
                    $li.remove();
                    updateCounters();
                }
            });
        }
    });


    loadTodos();
});