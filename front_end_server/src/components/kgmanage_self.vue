<template>
  <!-- 自己编写的知识管理页面 -->
  <div style="position: absolute; width: 100%; height:100%">
    <kgecharts :options="kgoptions1" :width="kgwidth" :height="kgheight" @clickNode="clickNode1" @dblclickNode="clickNode2"></kgecharts>
    <my-map-drawer placement="right">
      <div style="width: 500px; padding: 0px 2px;">
        <my-panel title="Operation" theme="background" icon="el-icon-s-tools">
          <el-input
            placeholder="请输入cypher查询语句"
            prefix-icon="el-icon-search"
            v-model="input_cypher"
            clearable>
            <i slot="suffix" class="el-input__icon el-icon-caret-right" @click="cypherSearch"></i>
          </el-input>
          <div class="demo-button" style="padding: 10px 10px;">
            <el-row>
                <el-col :span="4"><div style="font-weight: 900; font-size: 20px; margin-top: 5px; color: black;">视图：</div></el-col>
                <el-col :span="20">
                  <div>
                    <el-button type="primary" size="medium" round @click="clearView">清空视图</el-button>
                    <el-button type="primary" size="medium" round @click="reload">刷新</el-button>
                    <el-button type="danger" size="medium" round @click="matchNodeEdge">联合查询</el-button>
                    <my-dialog
                     :visible.sync="visible_edgenode_match"
                      target="body" 
                      title="联合查询" 
                      width="600px" height="500px" 
                      icon="el-icon-s-tools"
                      submitText="查询"
                      :modal="true"
                      @submit="matchEdgeNodeSubmit('ruleForm0')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm0">
                          <el-form-item label="头节点标签">
                            <el-input v-model="formLabelAlign.label" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="条件(Key:Value)">
                            <el-input v-model="formLabelAlign.whereAttribute" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="尾节点标签">
                            <el-input v-model="formLabelAlign.tlabel" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="条件(Key:Value)">
                            <el-input v-model="formLabelAlign.twhereAttribute" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="关系类型">
                            <el-input v-model="formLabelAlign.rtype" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="条件(Key:Value)">
                            <el-input v-model="formLabelAlign.rwhereAttribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                  </div>
                </el-col>
            </el-row>
            <hr style="FILTER: alpha(opacity=0,finishopacity=0,style=3)" width="100%" color='grey' SIZE=1>
            <el-row>
              <el-col :span="4"><div style="font-weight: 900; font-size: 20px; margin-top: 5px; color: black;">节点：</div></el-col>
                <el-col :span="20">
                  <div>
                    <el-button type="success" size="medium" round @click="node_add">添加</el-button>
                    <el-button type="success" size="medium" round @click="node_set">修改</el-button>
                    <el-button type="success" size="medium" round @click="node_del">删除</el-button>
                    <el-button type="success" size="medium" round @click="node_match">查询</el-button>
                    <my-dialog
                     :visible.sync="visible_node_add"
                      target="body" 
                      title="添加节点" 
                      width="600px" height="240px" 
                      icon="el-icon-s-tools"
                      submitText="创建"
                      :modal="true"
                      @submit="addNodeSubmit('ruleForm1')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm1">
                          <el-form-item label="标签" prop="label">
                            <el-input v-model="formLabelAlign.label" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="属性(Key:Value)" prop="attribute">
                            <el-input v-model="formLabelAlign.attribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                    <my-dialog
                     :visible.sync="visible_node_set"
                      target="body" 
                      title="修改节点" 
                      width="600px" height="240px" 
                      icon="el-icon-s-tools"
                      submitText="修改"
                      :modal="true"
                      @submit="setNodeSubmit('ruleForm2')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm2">
                          <el-form-item label="节点id" prop="id">
                            <el-input v-model="formLabelAlign.id" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="属性(Key:Value)" prop="attribute">
                            <el-input v-model="formLabelAlign.attribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                    <my-dialog
                     :visible.sync="visible_node_del"
                      target="body" 
                      title="删除节点" 
                      width="400px" height="180px" 
                      icon="el-icon-s-tools"
                      submitText="删除"
                      :modal="true"
                      @submit="delNodeSubmit('ruleForm3')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign" :rules="rules" ref="ruleForm3">
                          <el-form-item label="节点id" prop="id">
                            <el-input v-model="formLabelAlign.id" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                    <my-dialog
                     :visible.sync="visible_node_match"
                      target="body" 
                      title="查询节点" 
                      width="600px" height="240px" 
                      icon="el-icon-s-tools"
                      submitText="查询"
                      :modal="true"
                      @submit="matchNodeSubmit('ruleForm4')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm4">
                          <el-form-item label="标签" prop="label">
                            <el-input v-model="formLabelAlign.label" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="条件(Key:Value)">
                            <el-input v-model="formLabelAlign.whereAttribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                  </div>
                </el-col>
            </el-row>
            <hr style="FILTER: alpha(opacity=0,finishopacity=0,style=3)" width="100%" color='grey' SIZE=1>
            <el-row>
              <el-col :span="4"><div style="font-weight: 900; font-size: 20px; margin-top: 5px; color: black;">关系：</div></el-col>
                <el-col :span="20">
                  <div>
                    <el-button type="warning" size="medium" round @click="edge_add">添加</el-button>
                    <el-button type="warning" size="medium" round @click="edge_set">修改</el-button>
                    <el-button type="warning" size="medium" round @click="edge_del">删除</el-button>
                    <el-button type="warning" size="medium" round @click="edge_match">查询</el-button>
                  </div>
                  <my-dialog
                     :visible.sync="visible_edge_add"
                      target="body" 
                      title="添加关系" 
                      width="600px" height="350px" 
                      icon="el-icon-s-tools"
                      submitText="创建"
                      :modal="true"
                      @submit="addEdgeSubmit('ruleForm5')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm5">
                          <el-form-item label="头节点id" prop="hid">
                            <el-input v-model="formLabelAlign.hid" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="尾节点id" prop="tid">
                            <el-input v-model="formLabelAlign.tid" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="类型(Type)" prop="rtype">
                            <el-input v-model="formLabelAlign.rtype" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="属性(Key:Value)">
                            <el-input v-model="formLabelAlign.attribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                  <my-dialog
                     :visible.sync="visible_edge_set"
                      target="body" 
                      title="修改边" 
                      width="600px" height="240px" 
                      icon="el-icon-s-tools"
                      submitText="修改"
                      :modal="true"
                      @submit="setEdgeSubmit('ruleForm6')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm6">
                          <el-form-item label="边id" prop="id">
                            <el-input v-model="formLabelAlign.id" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="属性(Key:Value)" prop="attribute">
                            <el-input v-model="formLabelAlign.attribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                  <my-dialog
                     :visible.sync="visible_edge_del"
                      target="body" 
                      title="删除边" 
                      width="400px" height="180px" 
                      icon="el-icon-s-tools"
                      submitText="删除"
                      :modal="true"
                      @submit="delEdgeSubmit('ruleForm7')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign" :rules="rules" ref="ruleForm7">
                          <el-form-item label="边id" prop="id">
                            <el-input v-model="formLabelAlign.id" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                    <my-dialog
                     :visible.sync="visible_edge_match"
                      target="body" 
                      title="查询边" 
                      width="600px" height="240px" 
                      icon="el-icon-s-tools"
                      submitText="查询"
                      :modal="true"
                      @submit="matchEdgeSubmit('ruleForm8')"
                      @close="dialogClose"
                      @cancel="dialogClose">
                      <el-form :label-position="labelPosition" label-width="120px" :model="formLabelAlign" :rules="rules" ref="ruleForm8">
                          <el-form-item label="类型(Type)" prop="rtype">
                            <el-input v-model="formLabelAlign.rtype" clearable></el-input>
                          </el-form-item>
                          <el-form-item label="条件(Key:Value)">
                            <el-input v-model="formLabelAlign.whereAttribute" clearable></el-input>
                          </el-form-item>
                      </el-form>
                    </my-dialog>
                </el-col>
            </el-row>
            <hr style="FILTER: alpha(opacity=0,finishopacity=0,style=3)" width="100%" color='grey' SIZE=1>
            <el-row>
              <el-col :span="6"><div style="font-weight: 900; font-size: 20px; margin-top: 5px; color: black;">批处理：</div></el-col>
                <el-col :span="18">
                  <div>
                    <el-button type="danger" size="small" round @click="load_xlsx">XLSX</el-button>
                    <el-button type="danger" size="small" round @click="load_csv">CSV</el-button>
                    <el-button type="danger" size="small" round @click="load_shp">SHP</el-button>
                    <el-button type="danger" size="small" round @click="load_geojson">GEOJSON</el-button>
                  </div>
                  <my-dialog
                     :visible.sync="visible_load_xlsx"
                      target="body" 
                      title="导入表格" 
                      width="800px" height="600px" 
                      icon="el-icon-s-tools"
                      submitText="上传"
                      :modal="true"
                      @submit="load_xlsxSubmit"
                      @close="xlsxDialogClose"
                      @cancel="xlsxDialogClose">
                      <input type="file" id="xlsxfile" ref="uploadxlsx" :accept="fileType" @change="xlsxFileChange">
                      <el-table
                      :data="tableData"
                      style="width: 100%"
                      height="465"
                      v-loading="loading"
                      element-loading-text="拼命加载中"
                      element-loading-spinner="el-icon-loading"
                      element-loading-background="rgba(0, 0, 0, 0.8)">
                      <el-table-column
                        prop="head_node_label"
                        label="头节点标签">
                      </el-table-column>
                      <el-table-column
                        prop="head_node_attritute"
                        label="头节点属性">
                      </el-table-column>
                      <el-table-column
                        prop="r_type"
                        label="关系类型">
                      </el-table-column>
                      <el-table-column
                        prop="r_attritube"
                        label="关系属性">
                      </el-table-column>
                      <el-table-column
                        prop="tail_node_label"
                        label="尾节点标签">
                      </el-table-column>
                      <el-table-column
                        prop="tail_node_attribute"
                        label="尾节点属性">
                      </el-table-column>
                    </el-table>
                  </my-dialog>
                  <my-dialog
                     :visible.sync="visible_load_shp"
                      target="body" 
                      title="导入矢量" 
                      width="800px" height="600px" 
                      icon="el-icon-s-tools"
                      submitText="上传"
                      :modal="true"
                      @submit="load_shpSubmit"
                      @close="shpDialogClose"
                      @cancel="shpDialogClose">
                      <input type="file" ref="uploadshp" :accept="fileType" @change="shpFileChange">
                      <my-map
                      :zoom="1"
                      height="97%"
                      v-loading="loading"
                      element-loading-text="拼命加载中"
                      element-loading-spinner="el-icon-loading"
                      element-loading-background="rgba(0, 0, 0, 0.8)">
                        <my-map-geo :json="geo" :key="key"></my-map-geo>
                      </my-map>
                  </my-dialog>
                </el-col>
            </el-row>
          </div>
        </my-panel>
        <my-panel title="Node Information" theme="background" icon="el-icon-info">
          <my-key-val-list :column="nodecolumn" :data="nodedata" border :columns="1"> </my-key-val-list>
        </my-panel>
        <my-panel title="Relationship Information" theme="background" icon="el-icon-link">
          <my-key-val-list :column="edgecolumn" :data="edgedata" border :columns="1"> </my-key-val-list>
        </my-panel>
      </div>
    </my-map-drawer>
  </div>
</template>

<script>
import kgecharts from './kgecharts.vue'
import {options3} from '../assets/js/utilkg'
import axios from '$ui/utils/axios'
// import china from '$ui/charts/geo/china.json'
axios.defaults.baseURL = 'http://127.0.0.1:5000'

export default {
    components: {
      kgecharts
    },
    data() {
        return {
            kgIdList: new Set(),
            kgEdgeIdSet: new Set(),
            kgoptions1: options3,
            kgwidth: '100%',
            kgheight: '100%',
            nodecolumn: [],
            nodedata: {},
            edgecolumn: [],
            edgedata: {},
            input_cypher: null,
            visible_node_add: false,
            visible_node_del: false,
            visible_node_set: false,
            visible_node_match: false,
            visible_edge_add: false,
            visible_edge_del: false,
            visible_edge_set: false,
            visible_edge_match: false,
            visible_edgenode_match: false,
            visible_load_xlsx: false,
            visible_load_shp: false,
            labelPosition: 'right',
            formLabelAlign: {
              label: '',
              attribute: '',
              id: '',
              whereAttribute: '',
              hid: '',
              tid: '',
              rtype: '',
              tlabel: '',
              twhereAttribute: '',
              rwhereAttribute: '',
              key: 1
            },
            rules: {
              label: [{ required: true, message: '请输入节点标签', trigger: 'blur' }],
              attribute: [{required: true, message: 'eg:name:\'Ameracation\',task_id:\'demo\'', trigger: 'blur' }],
              id: [{ required: true, message: '请输入节点id', trigger: 'blur' }],
              hid: [{ required: true, message: '请输入头节点id', trigger: 'blur' }],
              tid: [{ required: true, message: '请输入尾节点id', trigger: 'blur' }],
              rtype: [{ required: true, message: '请输入边的类型', trigger: 'blur' }]
            },
            tableData: [{
              head_node_label: 'headLabel',
              head_node_attritute: 'name:\'头节点属性示例\'',
              r_type: 'relationType',
              r_attritube: 'name:\'relationshipAttribute\'',
              tail_node_label: 'tailLabel',
              tail_node_attribute: 'name:\'尾节点属性示例\''
            }, {
              head_node_label: 'country',
              head_node_attritute: 'name:\'中华人民共和国\'',
              r_type: 'province',
              r_attritube: 'name:\'省\'',
              tail_node_label: 'province',
              tail_node_attribute: 'name:\'湖北省\''
            }],
            dataLoading: false,
            filename: '',
            loading: false,
            fileType: '',
            geo: {}
        };
    },
    methods: {
        // 获取单个节点
        getOneNode(option, key, value, label) {
            axios.get('/manage/kg/getOneNode', {
            params: {
                label: label,
                key: key,
                value: value
            }
            })
            .then((response) => {
              if (this.kgIdList.has(response.data.data.id) === false) {
                  this.kgIdList.add(response.data.data.id)
                  option.series[0].data.push(response.data.data)
              }
            })
            .catch(function (error) {
                console.log(error);
            })
        },
      // 知识图谱节点展开接口
      kgAddNodes(option, id) {
        axios.get('/guotu/kg/update_from_nodeid', {
        params: {
          id: id
        }
        })
        .then((response) => {
          // for in 遍历的key为索引值
          for (const key1 of response.data.data) {
            if (this.kgIdList.has(key1.id) === false) {
                this.kgIdList.add(key1.id)
                option.series[0].data.push(key1)
            }
          }
          for (const key2 of response.data.links) {
            if (this.kgEdgeIdSet.has(key2.id) === false) {
                this.kgEdgeIdSet.add(key2.id)
                option.series[0].links.push(key2)
            }
          }
        })
        .catch(function (error) {
          console.log(error);
        })
      },
    // 单击查看节点详情
      clickNode1(nodeData) {
        if (nodeData.dataType === 'node') {
          axios.get('/manage/kg/getNodeInformation', {
          params: {
            nodeid: nodeData.data.id
          }
          })
          .then((response) => {
            this.nodedata = response.data.data
            this.nodecolumn = response.data.column
          })
          .catch(function (error) {
            console.log(error);
          })
        } else {
          axios.get('/manage/kg/getRelationshipInformation', {
          params: {
            relationshipId: nodeData.data.id,
            relationshipType: nodeData.data.value
          }
          })
          .then((response) => {
            this.edgedata = response.data.data
            this.edgecolumn = response.data.column
          })
          .catch(function (error) {
            console.log(error);
          })
        }
        
      },
    //   双击展开
      clickNode2(nodeData) {
        // console.log(this.kgoptions1)
        this.kgAddNodes(this.kgoptions1, nodeData.data.id)
      },
      // cypher查询
      // match(n:country) where n.name='Amer2' delete n
      cypherSearch() {
        if (!this.input_cypher) {
          this.$message.error('请输入查询语句')
        } else {
          axios.get('/manage/kg/runCypher', {
              params: {
                  cypher: this.input_cypher
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  this.visible_node_add = false
                  this.$message({
                    message: '执行成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('语法错误，执行失败')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
        }
      },
      clearView() {
        this.kgoptions1.series[0].data = []
        this.kgoptions1.series[0].links = []
        this.kgIdList.clear()
        this.kgEdgeIdSet.clear()
      },
      reload() {
        // 初始化知识图谱
        this.clearView()
        this.getOneNode(this.kgoptions1, 'alias', '中华人民共和国-country', 'country')
      },
      matchNodeEdge() {
        this.visible_edgenode_match = true
      },
      matchEdgeNodeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/matchEdgeNode', {
              params: {
                  hlabel: this.formLabelAlign.label,
                  hwhereAttribute: this.formLabelAlign.whereAttribute,
                  tlabel: this.formLabelAlign.tlabel,
                  twhereAttribute: this.formLabelAlign.twhereAttribute,
                  type: this.formLabelAlign.rtype,
                  rwhereAttribute: this.formLabelAlign.rwhereAttribute
              }
              })
              .then((response) => {
                this.clearView()
                this.kgoptions1.series[0].data = response.data.data
                this.kgoptions1.series[0].links = response.data.links
                for (const key1 of response.data.data) {
                  if (this.kgIdList.has(key1.id) === false) {
                      this.kgIdList.add(key1.id)
                  }
                }
                for (const key2 of response.data.links) {
                  if (this.kgEdgeIdSet.has(key2.id) === false) {
                      this.kgEdgeIdSet.add(key2.id)
                  }
                }
                this.visible_edgenode_match = false
                this.dialogClose()
                if (response.data.msg === '查询失败') {
                  this.$message.error(response.data.msg)
                } else {
                  this.$message({
                    message: response.data.msg,
                    type: 'success'
                  })
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      node_add() {
        this.visible_node_add = true
      },
      // name:'Ameracation1',task_id:'demo'
      addNodeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/createNode', {
              params: {
                  label: this.formLabelAlign.label,
                  attribute: this.formLabelAlign.attribute
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  this.kgoptions1.series[0].data.push(response.data.data)
                  this.kgIdList.add(response.data.data.id)
                  this.visible_node_add = false
                  this.formLabelAlign = {
                    label: '',
                    attribute: ''
                  }
                  this.$message({
                    message: '创建成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('创建失败')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      node_set() {
        this.visible_node_set = true
      },
      // name:'美国2', year:1111,area:123
      setNodeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/setNode', {
              params: {
                  id: this.formLabelAlign.id,
                  attribute: this.formLabelAlign.attribute
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  if (this.kgIdList.has(this.formLabelAlign.id)) {
                    const temp = []
                    for (const key1 of this.kgoptions1.series[0].data) {
                      if(key1.id !== this.formLabelAlign.id) {
                        temp.push(key1)
                      }
                    }
                    this.kgoptions1.series[0].data = temp
                    this.kgoptions1.series[0].data.push(response.data.data)
                    this.clickNode1({
                      dataType: 'node',
                      data: {id: this.formLabelAlign.id}
                    })
                  }
                  this.visible_node_set = false
                  this.formLabelAlign = {
                    label: '',
                    attribute: '',
                    id: ''
                  }
                  this.$message({
                    message: '修改成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('修改失败')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      node_del() {
        this.visible_node_del = true
      },
      delNodeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/delNode', {
              params: {
                  id: this.formLabelAlign.id
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  if (this.kgIdList.has(this.formLabelAlign.id)) {
                    this.kgIdList.delete(this.formLabelAlign.id)
                    const temp = []
                    for (const key1 of this.kgoptions1.series[0].data) {
                      if(key1.id !== this.formLabelAlign.id) {
                        temp.push(key1)
                      }
                    }
                    this.kgoptions1.series[0].data = temp
                  }
                  this.visible_node_del = false
                  this.formLabelAlign = {
                    label: '',
                    attribute: '',
                    id: ''
                  }
                  this.$message({
                    message: '删除成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('删除失败,节点有边或id不正确')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          } 
        })
      },
      node_match() {
        this.visible_node_match = true
      },
      // name:'中华人民共和国'
      matchNodeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/matchNode', {
              params: {
                  label: this.formLabelAlign.label,
                  whereAttribute: this.formLabelAlign.whereAttribute
              }
              })
              .then((response) => {
                this.clearView()
                this.kgoptions1.series[0].data = response.data.data
                for (const key1 of response.data.data) {
                  if (this.kgIdList.has(key1.id) === false) {
                      this.kgIdList.add(key1.id)
                  }
                }
                this.visible_node_match = false
                this.formLabelAlign = {
                    label: '',
                    whereAttribute: ''
                  }
                if (response.data.data.msg === '查询失败') {
                  this.$message.error(response.data.msg)
                } else {
                  this.$message({
                    message: response.data.msg,
                    type: 'success'
                  })
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      edge_add() {
        this.visible_edge_add = true
      },
      addEdgeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/createEdge', {
              params: {
                hid: this.formLabelAlign.hid,
                tid: this.formLabelAlign.tid,
                type: this.formLabelAlign.rtype,
                attribute: this.formLabelAlign.attribute
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  this.kgAddNodes(this.kgoptions1, this.formLabelAlign.hid)
                  this.visible_edge_add = false
                  this.dialogClose()
                  this.$message({
                    message: '创建成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('创建失败')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      edge_set() {
        this.visible_edge_set = true
      },
      setEdgeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/setEdge', {
              params: {
                  id: this.formLabelAlign.id,
                  attribute: this.formLabelAlign.attribute
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  if (this.kgEdgeIdSet.has(this.formLabelAlign.id)) {
                    const temp = []
                    for (const key1 of this.kgoptions1.series[0].links) {
                      if(key1.id !== this.formLabelAlign.id) {
                        temp.push(key1)
                      }
                    }
                    this.kgoptions1.series[0].links = temp
                    this.kgEdgeIdSet.delete(this.formLabelAlign.id)
                    this.kgAddNodes(this.kgoptions1, response.data.data.id)
                    this.clickNode1({
                      dataType: 'edge',
                      data: {id: this.formLabelAlign.id}
                    })
                  }
                  this.visible_edge_set = false
                  this.dialogClose()
                  this.$message({
                    message: '修改成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('修改失败')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      edge_del() {
        this.visible_edge_del = true
      },
      delEdgeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/delEdge', {
              params: {
                  id: this.formLabelAlign.id
              }
              })
              .then((response) => {
                if (response.data.data.msg === 200) {
                  if (this.kgEdgeIdSet.has(this.formLabelAlign.id)) {
                    this.kgEdgeIdSet.delete(this.formLabelAlign.id)
                    const temp = []
                    for (const key1 of this.kgoptions1.series[0].links) {
                      if(key1.id !== this.formLabelAlign.id) {
                        temp.push(key1)
                      }
                    }
                    this.kgoptions1.series[0].links = temp
                  }
                  this.edgedata = {}
                  this.edgecolumn = []
                  this.visible_edge_del = false
                  this.formLabelAlign = {
                    label: '',
                    attribute: '',
                    id: ''
                  }
                  this.$message({
                    message: '删除成功',
                    type: 'success'
                  })
                } else {
                  this.$message.error('删除失败')
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          } 
        })
      },
      edge_match() {
        this.visible_edge_match = true
      },
      matchEdgeSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.get('/manage/kg/matchEdge', {
              params: {
                  type: this.formLabelAlign.rtype,
                  whereAttribute: this.formLabelAlign.whereAttribute
              }
              })
              .then((response) => {
                this.clearView()
                this.kgoptions1.series[0].data = response.data.data
                this.kgoptions1.series[0].links = response.data.links
                for (const key1 of response.data.data) {
                  if (this.kgIdList.has(key1.id) === false) {
                      this.kgIdList.add(key1.id)
                  }
                }
                for (const key2 of response.data.links) {
                  if (this.kgEdgeIdSet.has(key2.id) === false) {
                      this.kgEdgeIdSet.add(key2.id)
                  }
                }
                this.visible_edge_match = false
                this.dialogClose()
                if (response.data.msg === '查询失败') {
                  this.$message.error(response.data.msg)
                } else {
                  this.$message({
                    message: response.data.msg,
                    type: 'success'
                  })
                }
              })
              .catch(function (error) {
                  console.log(error);
              })
          }
        })
      },
      dialogClose() {
        for(const i in this.formLabelAlign) {
          this.formLabelAlign[i] = ''
        }
      },
      load_xlsx() {
        this.visible_load_xlsx = true
        this.fileType = '.xlsx'
      },
      load_csv() {
        this.visible_load_xlsx = true
        this.fileType = '.csv'
      },
      load_xlsxSubmit() {
        if (this.dataLoading) {
          this.loading = true
          axios.get('/manage/kg/xlsxCreateKg', {
              params: {
              }
              })
              .then((response) => {
                for (const key1 of response.data.data) {
                  if (this.kgIdList.has(key1.id) === false) {
                      this.kgIdList.add(key1.id)
                      this.kgoptions1.series[0].data.push(key1)
                  }
                }
                this.loading = false
                this.$notify({
                  title: '成功',
                  message: '知识图谱录入完成',
                  type: 'success'
                })
                this.visible_load_xlsx = false
                this.xlsxDialogClose()
              })
              .catch(function (error) {
                  console.log(error);
                  this.loading = false
              })
        } else if (this.filename === '') {
          this.$message.error('请选择文件')
        } else {
          this.$message.warning('数据正在读取')
        }
      },
      xlsxDialogClose() {
        this.tableData = [{
              head_node_label: 'headLabel',
              head_node_attritute: 'name:\'头节点属性示例\'',
              r_type: 'relationType',
              r_attritube: 'name:\'relationshipAttribute\'',
              tail_node_label: 'tailLabel',
              tail_node_attribute: 'name:\'尾节点属性示例\''
            }, {
              head_node_label: 'country',
              head_node_attritute: 'name:\'中华人民共和国\'',
              r_type: 'province',
              r_attritube: 'name:\'省\'',
              tail_node_label: 'province',
              tail_node_attribute: 'name:\'湖北省\''
            }]
        this.dataLoading = false
        this.filename = ''
        this.loading = false
      },
      xlsxFileChange() {
        // 存在bug，无法获取文件的绝对路径，现状上传文件必须存在multimodal_data文件夹下
        // 获取上传控件dom
        const fileObj = this.$refs.uploadxlsx.files[0]
        this.filename = fileObj.name
        // console.log(fileObj)
        // let url = null;
        // if (window.createObjcectURL !== undefined) { 
        //     url = window.createOjcectURL(fileObj); 
        // } else if (window.URL !== undefined) { 
        //     url = window.URL.createObjectURL(fileObj); 
        // } else if (window.webkitURL !== undefined) { 
        //     url = window.webkitURL.createObjectURL(fileObj);
        // }
        //   const file = new File([url], fileObj.name, { type: 'xlsx' })
        //   console.log(file)
        this.loading = true
        // 应该把数据读取并发送给后端，而不是传文件名
        axios.get('/manage/kg/xlsxFileLoad', {
              params: {
                  filePath: fileObj.name,
                  fileType: this.fileType
              }
              })
              .then((response) => {
                this.tableData = response.data.data
                this.dataLoading = true
                this.loading = false
                this.$notify({
                  title: '读取成功',
                  message: '载入' + this.tableData.length + '条数据',
                  type: 'success'
                })
              })
              .catch(function (error) {
                  console.log(error);
                  this.loading = false
              })
      },
      load_shp() {
        this.visible_load_shp = true
        this.fileType = '.shp'
      },
      load_geojson() {
        this.visible_load_shp = true
        this.fileType = '.json, .geojson'
      },
      shpFileChange() {
        const fileObj = this.$refs.uploadshp.files[0]
        this.filename = fileObj.name
        this.loading = true
        axios.get('/manage/kg/shpFileLoad', {
              params: {
                  filePath: fileObj.name,
                  fileType: this.fileType
              }
              })
              .then((response) => {
                this.geo = response.data.data
                this.key = -this.key
                console.log(this.geo)
                this.dataLoading = true
                this.loading = false
                this.$notify({
                  title: '读取成功',
                  type: 'success'
                })
              })
              .catch(function (error) {
                  console.log(error);
                  this.loading = false
              })
      },
      load_shpSubmit() {
        if (this.dataLoading) {
          this.loading = true
          axios.get('/manage/kg/shpCreateKg', {
              params: {
              }
              })
              .then((response) => {
                for (const key1 of response.data.data) {
                  if (this.kgIdList.has(key1.id) === false) {
                      this.kgIdList.add(key1.id)
                      this.kgoptions1.series[0].data.push(key1)
                  }
                }
                this.loading = false
                this.$notify({
                  title: '成功',
                  message: '知识图谱录入完成',
                  type: 'success'
                })
                this.visible_load_shp = false
                this.shpDialogClose()
              })
              .catch(function (error) {
                  console.log(error);
                  this.loading = false
              })
        } else if (this.filename === '') {
          this.$message.error('请选择文件')
        } else {
          this.$message.warning('数据正在读取')
        }
      },
      shpDialogClose() {
        this.dataLoading = false
        this.filename = ''
        this.loading = false
        this.geo = {}
      }
    },
    created() {
        // 初始化知识图谱
        this.getOneNode(this.kgoptions1, 'alias', '中华人民共和国-country', 'country')
    },
    mounted() {

    }
  }
</script>

<style lang="scss" scoped>
.demo-button {
  /deep/ {
    .el-row {
        margin-bottom: 10px;
    
        &:last-child {
          margin-bottom: 0;
        }
      }
      .el-button + .el-button {
        margin-left: 10px;
      }
      .el-button-group {
        .el-button + .el-button {
          margin-left: 0;
        }
    
        & + .el-button-group {
          margin-left: 10px;
        }
      }
  }
}
</style>
