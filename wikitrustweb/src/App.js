import React, { useState, useEffect } from 'react';
import axios from 'axios';
function App() {
  const [data, setData] = useState({ documents: [], articles: []});
  useEffect(() => {
    const fetchData = async () => {
      const result_a = await axios(
        'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/diffs/',
      );
      const result_b = await axios(
        'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/articles/',
      );
      setData(result_a.data);
      setData(result_b.data);
    };
    fetchData();
  }, []);
  return (
    <ul>
      {data.documents.map(item => (
        <li key={item.name}>
          <h1>Trust: {item.fields.trust.doubleValue}</h1>
          <p>Diff: {item.fields.diff_moves.bytesValue}</p>
        </li>
      ))}
    </ul>
  );
}
export default App;