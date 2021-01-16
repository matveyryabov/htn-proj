import logo from './logo.svg';
import './App.css';
import ImgUpl from './components/Image-upload/ImgUpl'
import UseCamera from './components/Camera/Camera'
import {Todo} from './components/InputForm/Todo';
import {Show} from './components/EditDelete/Show';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/'>
            <UseCamera/>
            <ImgUpl/>
            <Todo/>
          </Route>
          <Route path='/:id'>
            <Show/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
