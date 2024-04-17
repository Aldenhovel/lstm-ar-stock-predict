import React from "react";
import eventBus from "./eventBus";

import { Icon } from '@ant-design/compatible';
import { Menu} from 'antd';
import MenuItem from "antd/lib/menu/MenuItem";
import {FundOutlined, ReadOutlined, SettingOutlined, SlidersOutlined, StepBackwardOutlined} from "@ant-design/icons";
const SubMenu = Menu.SubMenu;


class Nav extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }

        this.items = {

        }
    }

    handleClick = (e) => {
        console.log('click ', e);
    }

    handleSwitchPage = (e) => {
        eventBus.emit('switch-page', {to: e.key});
        //eventBus.emit('clear-state', {});
    }


    render() {
        return (
            <Menu
                style={{
                    width: '100wh',
                    height: '100vh',
                    fontSize: '18px',
                    fontFamily: "'Euclid', sans-serif"
                }}
                defaultOpenKeys={['inference']}
                defaultSelectedKeys={['greedySearch']}
                mode="inline"
            >
                <SubMenu key={"inference"} style={{ fontSize: '18px', fontFamily: "'Euclid', sans-serif" }} title={<span><FundOutlined></FundOutlined><span>Inference</span></span>}>
                    <MenuItem key="greedySearch" onClick={this.handleSwitchPage} style={{ fontSize: '18px', fontFamily: "'Euclid', sans-serif" }}>
                        <SlidersOutlined></SlidersOutlined>
                        <span>Greedy Search</span>
                    </MenuItem>
                    <Menu.Item key="beamSearch" onClick={this.handleSwitchPage} style={{ fontSize: '18px', fontFamily: "'Euclid', sans-serif" }}>
                        <SlidersOutlined></SlidersOutlined>
                        <span>Beam Search</span>
                    </Menu.Item>
                </SubMenu>

                <MenuItem key="settings" onClick={this.handleSwitchPage} style={{ fontSize: '18px', fontFamily: "'Euclid', sans-serif" }}>
                    <SettingOutlined></SettingOutlined>
                    <span>Settings</span>
                </MenuItem>
                <MenuItem key="information" onClick={this.handleSwitchPage} style={{ fontSize: '18px', fontFamily: "'Euclid', sans-serif" }}>
                    <ReadOutlined></ReadOutlined>
                    <span>Information</span>
                </MenuItem>
            </Menu>
        )
    }


}

export default Nav;