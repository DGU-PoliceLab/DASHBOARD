import Cpu from "./components/system/cpu";
import "./App.css";

function App() {
    return (
        <div className="App">
            <div className="headerContainer"></div>
            <div className="contentContainer">
                <div className="systemSection">
                    <Cpu />
                </div>
                <div className="containerSection"></div>
                <div className="moduleSection"></div>
                <div className="edgecamSection"></div>
            </div>
        </div>
    );
}

export default App;
