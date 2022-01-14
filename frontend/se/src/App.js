import logo from './logo.svg';
import './App.css';
import React from 'react';
import { render } from '@testing-library/react';
import axios from 'axios';  

const host = 'https://glacial-meadow-24383.herokuapp.com'

class SearchBar extends React.Component{

  constructor(props){
    super(props);
    this.state = {result: ''}
  }

  handleChange = (e) =>{
    this.setState({result: e.target.value});
    this.props.setSearchValue(e.target.value);
  }

  handleSubmit = () =>{
    this.props.handleSubmitFromForm(this.state.result);
  }

  render(){
    return (
      <div>
        <div>
          <div>
            <div>
              <label>Search</label>
              <input
                type='text'
                value={this.state.result}
                onChange={this.handleChange}
              />
            </div>
            <div>
              <button
                
                onClick={this.handleSubmit}
              >
                Search
              </button>
            </div>
          </div>
        </div>
      </div>)
  }

}

class DashBoard extends React.Component{

  constructor(props){
    super(props);
    this.state = {results: []}

  }

  searchValue = (query) => {
    if(query === ''){
      this.setState({results:[]});
      return;
    }

    
    const json = {'query': query}
    const jsonStr = JSON.stringify(json);

    
         
          axios.post(host + '/search', jsonStr, {
            headers: {
              'Content-Type': 'application/json'
            }
          }).then((response) => {
            console.log(response.data);
            this.setState({results: response.data.result});
  
          }, 
          (error)=>{
            console.log(error);
           
          })


    


  }
  

   render(){
     
     
     return( 
       <div>
                <div>
                <SearchBar handleSubmitFromForm={this.searchValue}
                  setSearchValue={this.searchValue}
                />
          </div>
          <div>
            <ResultList 
            results={this.state.results}/>
          </div>
       </div>

     )
   }
}


class ResultList extends React.Component{
  constructor(props){
    super(props);

  }


  render(){
    const results = this.props.results.map((result)=>(
        <Result result={result}/>
    ));

    return (<div id="results">{results}</div>)
  }

}

class Result extends React.Component{

  render(){
    return (
      <div>
        <div>
          
          <div>
            <span>
              {this.props.result}
            </span>
          </div>
        </div>
      </div>
    );
  }


} 
class App extends React.Component{
  constructor(props){
    super(props)
  
  }

  render(){
    return (<div>
     <DashBoard/>
    </div>)
  }


}
export default App;
