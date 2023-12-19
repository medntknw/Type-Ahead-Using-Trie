import "./SearchResultList.css";
import SearchResult from "./SearchResult";

function SearchResultList ({ results }) {
  return (
    <div className="results-list">
      {results.map((result, id) => {
        return <SearchResult result={result.name} key={id} />;
      })}
    </div>
  );
};
export default SearchResultList;