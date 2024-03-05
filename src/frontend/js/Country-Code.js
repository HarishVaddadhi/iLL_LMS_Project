let countryCodes;

// Fetch country codes JSON
fetch('../json/CountryCodes.json')
  .then(response => response.json())
  .then(data => {
    countryCodes = data;
    initializeCountryCodeDropdown(); 
  });

function initializeCountryCodeDropdown() {
  let select = document.getElementById("country-code");

  countryCodes.forEach(country => {
    let option = document.createElement("option");
    option.value = country.dial_code;
    option.text = country.name + " - " + country.dial_code; 

    select.appendChild(option);
  }); 
}

