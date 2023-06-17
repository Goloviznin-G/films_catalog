const setURLParams = (newParams, toDelFields = []) => {
    let currParams = window.location.search;
    if (currParams) {
        currParams = currParams.includes('?') ? currParams.substring(1) : currParams;
        const keyValPairs = currParams.split('&');
        const tempMap = {};
        keyValPairs.forEach(pair => {
            var [key, val] = pair.split("=");
            tempMap[key] = val;
        });
        const result = {
            ...tempMap,
            ...newParams
        }
        if (toDelFields.length) {
            toDelFields.forEach(fld => {
                delete result[fld];
            });
        }
        return new URLSearchParams(result).toString();
    }
    return new URLSearchParams(newParams).toString();
};

const searchName = () => {
    let prevValue = '';
    return function returnValue(value) {
        if (value || value == '') {
            prevValue = value;
            return value;
        } else {
            return prevValue;
        }
    }
};

const handleSearchChange = searchName();

const filterFilms = (field, optValue) => {
    switch(field) {
        case 'search':
            const input_value = document.getElementById("search").value;
            const value = handleSearchChange(input_value);
            if(value) {
                window.location = `/film/?${setURLParams({'search': value})}`;
            } else {
                window.location = `/film/?${setURLParams({}, ['search'])}`;
            }
            break;
        }
    }

const SPECIAL_DO_NOT_ADD_SIGN = "!del";

const sortAscDesc = (field) => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  if (urlParams.get('sort_order') == 'desc') {
    return {
      "sort": SPECIAL_DO_NOT_ADD_SIGN,
      "sort_order": SPECIAL_DO_NOT_ADD_SIGN
    };
  }

  return {
    "sort": field,
    "sort_order": urlParams.get('sort_order') == 'asc' ? "desc" : 'asc'
  }
};

const sortFilms = (field) => {
  let urlParams = '';
  const sortFields = sortAscDesc(field);

  if (sortFields["sort"] == SPECIAL_DO_NOT_ADD_SIGN) {
    urlParams = setURLParams({}, ["sort", "sort_order"]);
  } else {
    urlParams = setURLParams(sortFields);
  }

  window.location = `/film/?${urlParams}`;
};

const setFilmsPage = (page) => {
  const urlParams = setURLParams({
    'page': page
  });

  window.location = `/film/?${urlParams}`;
};