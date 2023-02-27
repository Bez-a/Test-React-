import './App.css';
import data from './data';
import AnimalCard from '../AnimalCard/AnimalCard';

function App() {
  return (
    <div className="wrapper">
      <h1>Animals</h1>
      {data.map(animal => (
        <AnimalCard key={animal.name}
        name={animal.name}
        scientificName={animal.scientificName}
        additional={animal.additional}
        diet={animal.diet}
        size={animal.size}
        />
      ))}
    </div> 
  );
}

export default App;
