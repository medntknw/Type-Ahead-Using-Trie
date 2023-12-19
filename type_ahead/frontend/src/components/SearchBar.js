import { useState } from "react";
import { FaSearch } from "react-icons/fa";

import "./SearchBar.css";

function SearchBar ({ setResults }){
  const [input, setInput] = useState("");

  const fetchData = (value) => {
    fetch("https://localhost.com/suggest")
      .then((response) => response.json())
      .then((json) => {
        const results = json.suggest
        setResults(results);
      });
  };

  const handleChange = (value) => {
    setInput(value);
    fetchData(value);
  };

  return (
    <div className="input-wrapper">
      <FaSearch id="search-icon" />
      <input
        placeholder="Type to search..."
        value={input}
        onChange={(e) => handleChange(e.target.value)}
      />
    </div>
  );
};
export default SearchBar;