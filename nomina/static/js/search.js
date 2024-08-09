document.addEventListener("DOMContentLoaded", function () {
  const parametersContainer = document.getElementById("parameters-container");
  const addParameterButton = document.getElementById("add-parameter");
  let parameterCount = 0;

  addParameterButton.addEventListener("click", function () {
    addParameterField();
  });

  function addParameterField() {
    parameterCount++;

    const parameterDiv = document.createElement("div");
    parameterDiv.classList.add("parameter");

    const entitySelect = document.createElement("select");
    entitySelect.name = `entity_${parameterCount}`;
    entitySelect.innerHTML = `
            <option value="">Seleccione entidad</option>
            <option value="employee">Empleado</option>
            <option value="department">Departamento</option>
            <option value="position">Posición</option>
            <option value="income">Ingreso</option>
            <option value="deduction">Deducción</option>
        `;

    const valueSelect = document.createElement("select");
    valueSelect.name = `value_${parameterCount}`;
    valueSelect.disabled = true;

    entitySelect.addEventListener("change", function () {
      loadOptions(valueSelect, entitySelect.value);
    });

    const removeButton = document.createElement("button");
    removeButton.classList.add("remove-button");
    removeButton.type = "button";
    removeButton.innerHTML = "&times;";
    removeButton.addEventListener("click", function () {
      parametersContainer.removeChild(parameterDiv);
    });

    parameterDiv.appendChild(entitySelect);
    parameterDiv.appendChild(valueSelect);
    parameterDiv.appendChild(removeButton);
    parametersContainer.appendChild(parameterDiv);
  }

  function loadOptions(selectElement, entity) {
    selectElement.innerHTML = '<option value="">Cargando...</option>';
    selectElement.disabled = false;

    const url = `${get_options_url}?entity=${entity}`;

    fetch(url, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        selectElement.innerHTML = data.options
          .map(
            (option) =>
              `<option value="${option.value}">${option.label}</option>`,
          )
          .join("");
      });
  }
});
