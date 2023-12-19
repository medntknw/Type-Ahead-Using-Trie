import { useState } from "react";
import { FaSearch } from "react-icons/fa";

import "./SearchBar.css";

function SearchBar ({ setResults }){
  const [input, setInput] = useState("");
  const [addDisabled, setAddDisabled] = useState(false);

  const fetchData = (value) => {
    fetch(`/api/suggest?q=${value}`)
      .then((response) => response.json())
      .then((json) => {
        const results = json.suggest
        setResults(results);
      });
  };

  const submitSearch = (value) => {
    setAddDisabled(true);
    fetch("/api/suggest", {
    method: "post",
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        query: value
    })
    })
    .then((response) => response.json())
    .then((json) => {
      setAddDisabled(false);
    });
  };

  const handleChange = (value) => {
    setInput(value);
    fetchData(value);
  };

  const handleSubmit = (value) => {
    submitSearch(value);
  }

  return (
    <div className="input-wrapper">
      <FaSearch id="search-icon" />
      <input
        placeholder="Type to search..."
        value={input}
        onChange={(e) => handleChange(e.target.value)}
      />
      <button disabled={addDisabled} type='submit' onClick={() => handleSubmit(input)}>Add</button>
    </div>
  );
};
export default SearchBar;