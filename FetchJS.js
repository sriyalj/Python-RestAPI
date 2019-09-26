const fetch = require("node-fetch");


function status(response) {
  return Promise.resolve(response)
}

function json(response) {
  return response.json()
}

fetch('http://localhost:5002/user/add', {
       headers: { "Content-Type": "application/json; charset=utf-8" },
       method: 'POST',
       body: JSON.stringify({
                 user_name: 'Sriyal',
                 password: 'Sriyal_123',
       })
})
.then(status)
.then(json)
.then(function(data) {
      console.log('\nJSON response Fetch for /user/add : ', data);
})
.catch(function(error) {
    console.log('\n\nRequest failed', error);
});


fetch('http://localhost:5002/login', {
       headers: { "Content-Type": "application/json; charset=utf-8" },
       method: 'POST',
       body: JSON.stringify({
                 user_name: 'Sriyal',
                 password: 'Sriyal_123',
       })
})
.then(status)
.then(json)
.then(function(data) {
      console.log('\n\nJSON response Fetch for /login : ', data);
})
.catch(function(error) {
    console.log('Request failed', error);
});

function timeout(ms, promise) {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      reject(new Error("timeout"))
    }, ms)
    promise.then(resolve, reject)
  })
}

timeout(30000, fetch('http://localhost:5002/login', {
                    headers: { "Content-Type": "application/json; charset=utf-8" },
                    method: 'POST',
                    body: JSON.stringify({
                              user_name: 'Sriyal',
                              password: 'Sriyal_123',
                    })
                  })
                  .then(status)
                  .then(json)
                  .then(function(data) {
                       console.log('\n\nJSON response Fetch for /login after 15s : ', data);
                  })
.                 catch(function(error) {
                       console.log('Request failed', error);
                  })
         )
            
fetch('http://localhost:5002/user/update', {
       headers: { "Content-Type": "application/json; charset=utf-8" },
       method: 'POST',
       body: JSON.stringify({
                 user_name: 'Sriyal',
                 password: 'Sriyal_123',
                 newpassword : "Sri_456",
       })
})
.then(status)
.then(json)
.then(function(data) {
      console.log('\n\nJSON response Fetch for /user/update : ', data);
})
.catch(function(error) {
    console.log('Request failed', error);
});

