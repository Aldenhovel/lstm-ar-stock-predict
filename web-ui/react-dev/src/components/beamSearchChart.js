import React from "react";
import {Row, Col, Select, Button} from "antd";
import {Card} from "antd";
import {Input} from "antd";
import {DatePicker} from "antd";
import {Badge, InputNumber} from "antd";
import {defaultBeamSearchOption} from "./chartOptions";
import * as echarts from 'echarts'
import dayjs from "dayjs";

import axios from "axios";

class BeamSearchChart extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            width: '100vw',
            height: '700px',
            backgroundColor: 'white',

            cDefault: 'default',
            cModelSelect: [
                {label: 'default', value: 'default'},
            ],

            data: {
                checkpoint: 'default',
                searchStep: 10,
                beamSize: 20,
                code: '300001',
                codePostfix: '.SZ',
                date: {
                    dateY: 2024,
                    dateM: 4,
                    dateD: 15,
                },
            },

            chartOptionBS: defaultBeamSearchOption,
            isLoading: false,

            myChart: null,
        }
    }

    onChange = (e) => {
        console.log(e);
    }


    handleSetChart = (option) => {
        this.state.myChart && this.state.myChart.setOption(option);
    }

    handleChangeBeamSize = (e) => {
        this.setState((prevState) => {
            const newState = {...prevState};
            newState.data.beamSize = e;
            return newState;
        })
    }

    handleChangeDate = (e) => {
        this.setState((prevState) => {
            const newState = {...prevState};
            newState.data.date.dateY = e.$y;
            newState.data.date.dateM = e.$M + 1;
            newState.data.date.dateD = e.$D;
            return newState;
        })
        //this.onChange(this.state.data);
    }

    handleChangeCheckpoint = (e) => {
        this.setState((prevState) => {
            const newState = {...prevState};
            newState.data.checkpoint = e;
            return newState;
        })
        //this.onChange(this.state.data);
    }

    handleCheckAvailableCheckpoint = (e) => {
        this.setState({cModelSelect: []})
        axios.get('/getCheckpointsItems')
            .then(response => {
                let cModelSelect = [];
                let ckpts = response.data.checkpoints;

                for (let i = 0; i < ckpts.length; i++) { cModelSelect.push({label: ckpts[i], value: ckpts[i]}) }
                this.setState((prevState) => {
                    const newState = {...prevState};
                    newState.cModelSelect = cModelSelect;
                    return newState
                })
            })
            .catch(error => {
                console.log(error);
            })
    }

    handleProcess = () => {

        this.setState({isLoading: true});
        let profile = {
            checkpoint: this.state.data.checkpoint,
            searchStep: this.state.data.searchStep,
            code: this.state.data.code,
            dateY: this.state.data.date.dateY,
            dateM: this.state.data.date.dateM,
            dateD: this.state.data.date.dateD,
            beamSize: this.state.data.beamSize,
        };
        //console.log(profile);
        axios.post('/processBeamSearch', profile)
            .then(response => {
                this.setState((prevState) => {

                    const newState = {...prevState};
                    newState.chartOptionBS.xAxis.data = response.data.xaxis;

                    let pds = response.data.pd;
                    let seriesData = [{
                        type: 'candlestick',
                        data: response.data.gt,
                    }];
                    for (let i=0; i < pds.length; ++i) {
                        let pd = [];
                        for (let j = 0; j < response.data.gt.length; j++) { pd.push(undefined) }
                        for (let j = 0; j < pds.length; j++) { pd.push(pds[i][j]) }
                        seriesData.push({
                            type: 'line',
                            data: pd,
                        })
                    }

                    newState.chartOptionBS.series = seriesData;
                    this.handleSetChart(this.state.chartOptionBS);
                    return newState;
                })

            })
            .catch(error => {
                console.log(error);
            })
        this.setState({isLoading: false});
    }

    handleChangeSearchStep = (e) => {
        this.setState((prevState) => {
            const newState = {...prevState};
            newState.data.searchStep = e;
            return newState;
        })
        //this.onChange(this.state.data);
    }

    handleChangeCode = (e) => {
        let code = e.target.value;
        let postfix = ''
        switch (code.slice(0, 2)) {
            case '00':
                postfix = ".SZ";
                break;
            case '30':
                postfix = '.SZ';
                break;
            case '60':
                postfix = '.SH';
                break;
            case '68':
                postfix = '.SH';
                break;
            default:
                postfix = '--';
                break
        }
        this.setState((prevState) => {
            const newState = {...prevState};
            newState.data.code = code;
            newState.data.codePostfix = postfix;
            return newState;
        })
        //this.onChange(this.state.data);
    }

    componentDidMount() {
        let chartDom = document.getElementById('chart');
        let myChart = echarts.init(chartDom);
        this.setState({ myChart });
    }

    render() {
        return (
            <div style={{
                width: this.state.width,
                height: this.state.height,
                backgroundColor: this.state.backgroundColor
            }}>
                <Row style={{height: this.state.height}}>
                    <Col xxl={4} xl={5} lg={6} md={6} sm={8} xs={8}>
                        <Card title={"Model Settings"} bordered={true}
                              style={{width: '95%', margin: '10px auto', backgroundColor: '#F0F0F0'}}>
                            <Badge status="success" text="Checkpoint"/><br/>
                            <Select defaultValue={this.state.cDefault} style={{width: '90%', margin: '5px 0'}}
                                    options={this.state.cModelSelect}
                                    onChange={this.handleChangeCheckpoint}
                                    onDropdownVisibleChange={this.handleCheckAvailableCheckpoint}
                            ></Select>
                            <Badge status="success" text="Search Steps"/><br/>
                            <InputNumber min={1} max={50} defaultValue={10} onChange={this.handleChangeSearchStep} changeOnWheel/>

                            <br/>
                            <Badge status="success" text="Beam Size"/><br/>
                            <InputNumber min={1} max={50} defaultValue={20} onChange={this.handleChangeBeamSize} changeOnWheel/>
                        </Card>


                        <Card title={"Data Settings"} bordered={true}
                              style={{width: '95%', margin: '10px auto', backgroundColor: '#F0F0F0'}}>
                            <Badge status="success" text="Code"/><br/>
                            <Input addonAfter={this.state.data.codePostfix} defaultValue="300001"
                                   style={{width: '90%', margin: '5px 0'}} onChange={this.handleChangeCode}/>
                            <Badge status="success" text="Date"/><br/>
                            <DatePicker defaultValue={dayjs('2024-4-15')} onChange={this.handleChangeDate} style={{width: '90%', margin: '5px 0'}}/>
                        </Card>

                        <Card bordered={true} style={{width: '95%', margin: '10px auto', backgroundColor: '#F0F0F0'}}>
                            <Button block loading={this.state.isLoading} onClick={this.handleProcess} type={"primary"} style={{width: '100%', margin: '0 auto'}}>Process</Button>
                        </Card>


                    </Col>
                    <Col xxl={16} xl={14} lg={12} md={18} sm={16} xs={16}>
                        <Card style={{
                            width: '90%',
                            height: '600px',
                            margin: '10px',
                            padding: '0',
                            backgroundColor: '#F0F0F0'
                        }} bordered={true}>
                            <div id="chart" style={{backgroundColor: 'white', width: '100%', height: '550px',}}></div>
                        </Card>
                    </Col>
                </Row>
            </div>
        )
    }
}

export default BeamSearchChart;