import React from "react"
import Radium from "radium"

import { connect } from "react-redux"

import * as counterActions from "../actions/counterActions"
import * as githubActions from "../actions/githubActions"
import Headline from "../components/Headline"
import GithubRepos from "../components/GithubRepos"

const styles = {
  button: {
    cursor: "pointer",
  },
  counter: {
    color: "blue",
    fontSize: "20px",
  }
}

@connect(state => ({
  counters: state.counters,
  github: state.github,
}))
@Radium
export default class SampleAppContainer extends React.Component {
  handleClick() {
    let {dispatch} = this.props;
    dispatch(counterActions.increaseCounter())
  }
  componentDidMount() {
    let {dispatch, github} = this.props
    if (!github.isLoadingRepos && github.repos === undefined) {
      dispatch(githubActions.fetchRepos())
    }
  }

  renderLoading() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            Loading...
          </div>
        </div>
      </div>
    )
  }

  render() {
    let {counters, github} = this.props
    if (github.isLoadingRepos || github.repos === undefined) {
      return this.renderLoading()
    }
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Sample App!</Headline>
            <div style={[styles.button]} onClick={() => this.handleClick()}>INCREASE</div>
            <p style={[styles.counter]}>{counters.clicks}</p>
            <p>{process.env.BASE_API_URL}</p>
            {github.repos !== undefined &&
              <GithubRepos repos={github.repos} />
            }
          </div>
        </div>
      </div>
    )
  }
}