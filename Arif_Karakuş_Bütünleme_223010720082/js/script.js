fetch('/users')
   .then(response => response.json())
   .then(data => {
        const userList = document.getElementById('user-list');
        data.forEach(user => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.email}</td>
            `;
            userList.appendChild(row);
        });
    });

document.querySelector('form').addEventListener('submit', event => {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/settings', {
        method: 'POST',
        body: formData
    })
   .then(response => response.json())
   .then(data => console.log(data));
});