import React, { useState, useEffect } from 'react';
import axios from 'axios';
function App() {
  const [diffs, setDiffs] = useState('');
  const [articles, setArticles] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const result_a = await axios(
        'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/diffs/',
      );
      const result_b = await axios(
        'https://firestore.googleapis.com/v1/projects/wikitrustapp/databases/(default)/documents/articles/',
      );
      // console.log(result_b.data);
      setDiffs(result_a.data);
      setArticles(result_b.data);
    };
    fetchData();
  }, []);

  return (
    <ul>
      {diffs ? diffs.documents.map(item => (
        <li key={item.name}>
          <h1>Trust: {item.fields.trust.doubleValue}</h1>
          <p>Diff: {item.fields.diff_moves.bytesValue}</p>
        </li>
      )) : 'LOADING...'}
      {articles ? articles.documents.map(item => (
        <li key={item.name}>
          <h1>Title: {item.fields.title.stringValue}</h1>
          <p>Text: {item.fields.text.stringValue}</p>
        </li>
      )) : 'LOADING...'}
    </ul>
  );
}
export default App;