export const options1 = {
  title: {
    text: ''
  },
  tooltip: {},
  toolbox: {
    show: true,
    feature: {
      restore: {
        show: true
      },
      saveAsImage: {
        show: true
      }
    }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District', 'Street', 'Region', 'Statistics', 'Proxy'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        },
        {
          name: 'Street'
        },
        {
          name: 'Region'
        },
        {
          name: 'Statistics'
        },
        {
          name: 'Proxy'
        }
      ],
      data: null,
      links: null
    }
  ]
};

export const options2 = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  toolbox: {
    show: true,
    feature: {
      restore: {
        show: true
      },
      saveAsImage: {
        show: true
      }
    }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District', 'Street', 'Region', 'Statistics', 'Proxy'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        },
        {
          name: 'Street'
        },
        {
          name: 'Region'
        },
        {
          name: 'Statistics'
        },
        {
          name: 'Proxy'
        }
      ],
      data: null,
      links: null
    }
  ]
};

export const options3 = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  toolbox: {
    show: true,
    feature: {
      restore: {
        show: true
      },
      saveAsImage: {
        show: true
      }
    },
    left: '5%'
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District', 'Street', 'Region', 'Statistics', 'Proxy', '幼儿园', '小学', '中学', '中专', '大专院校', '驾校', '党校', 'State', 'FreeState'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        },
        {
          name: 'Street'
        },
        {
          name: 'Region'
        },
        {
          name: 'Statistics'
        },
        {
          name: 'Proxy'
        },
        {
          name: '幼儿园'
        },
        {
          name: '小学'
        },
        {
          name: '中学'
        },
        {
          name: '中专'
        },
        {
          name: '大专院校'
        },
        {
          name: '驾校'
        },
        {
          name: '党校'
        },
        {
          name: 'State'
        },
        {
          name: 'FreeState'
        }
      ],
      data: [],
      links: []
    }
  ]
};

export const qaoptions = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District', 'Street', 'Region', 'Statistics', 'Proxy', '幼儿园', '小学', '中学', '中专', '大专院校', '驾校', '党校', 'State', 'FreeState'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'horizontal',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        },
        {
          name: 'Street'
        },
        {
          name: 'Region'
        },
        {
          name: 'Statistics'
        },
        {
          name: 'Proxy'
        },
        {
          name: '幼儿园'
        },
        {
          name: '小学'
        },
        {
          name: '中学'
        },
        {
          name: '中专'
        },
        {
          name: '大专院校'
        },
        {
          name: '驾校'
        },
        {
          name: '党校'
        },
        {
          name: 'State'
        },
        {
          name: 'FreeState'
        }
      ],
      data: [],
      links: []
    }
  ]
};

export const optionsProduct1 = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Product', 'Attribute'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Product'
        },
        {
          name: 'Attribute'
        }
      ],
      data: [],
      links: []
    }
  ]
};

export const optionsProduct2 = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Product', 'RecommendationProduct'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Product'
        },
        {
          name: 'RecommendationProduct'
        }
      ],
      data: [],
      links: []
    }
  ]
};

export const kgoptions2 = {
  title: {
    text: ''
  },
  tooltip: {},
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District', 'Street', 'Region', 'Statistics', 'Proxy'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: true, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbolSize: [4, 50],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        },
        {
          name: 'Street'
        },
        {
          name: 'Region'
        },
        {
          name: 'Statistics'
        },
        {
          name: 'Proxy'
        }
      ],
      data: [
        {
          name: '徐贱云'
        },
        {
          name: '冯可梁',
          category: 0
        },
        {
          name: '邓志荣',
          category: 0
        },
        {
          name: '李荣庆',
          category: 0
        },
        {
          name: '郑志勇',
          category: 1
        },
        {
          name: '赵英杰',
          category: 1
        },
        {
          name: '王承军',
          category: 1
        },
        {
          name: '陈卫东',
          category: 1
        },
        {
          name: '邹劲松',
          category: 2
        },
        {
          name: '赵成',
          category: 2
        },
        {
          name: '陈现忠',
          category: 2
        },
        {
          name: '陶泳',
          category: 2
        },
        {
          name: '王德福',
          category: 2
        }
      ],
      links: [
        {
          source: 0,
          target: 1,
          value: '夫妻'
        },
        {
          source: 0,
          target: 2,
          value: '子女'
        },
        {
          source: 0,
          target: 3,
          value: '夫妻'
        },
        {
          source: 0,
          target: 4,
          value: '父母'
        },
        {
          source: 1,
          target: 2,
          value: '表亲'
        },
        {
          source: 0,
          target: 5,
          value: '朋友'
        },
        {
          source: 4,
          target: 5,
          value: '朋友'
        },
        {
          source: 2,
          target: 8,
          value: '叔叔'
        },
        {
          source: 0,
          target: 12,
          value: '朋友'
        },
        {
          source: 6,
          target: 11,
          value: '爱人'
        },
        {
          source: 6,
          target: 3,
          value: '朋友'
        },
        {
          source: 7,
          target: 5,
          value: '朋友'
        },
        {
          source: 9,
          target: 10,
          value: '朋友'
        },
        {
          source: 3,
          target: 10,
          value: '朋友'
        },
        {
          source: 2,
          target: 11,
          value: '同学'
        }
      ]
    }
  ]
};

export const optionsKgCompute = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  toolbox: {
    show: true,
    feature: {
      restore: {
        show: true
      },
      saveAsImage: {
        show: true
      }
    }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 400,
        friction: 0.2
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        }
      ],
      data: null,
      links: null
    }
  ]
};

export const optionsErrorKg = {
  title: {
    text: ''
  },
  tooltip: {
    formatter: function(x) {
      return x.data.des;
  }
  },
  toolbox: {
    show: true,
    feature: {
      restore: {
        show: true
      },
      saveAsImage: {
        show: true
      }
    }
  },
  animationDurationUpdate: 1500,
  animationEasingUpdate: 'quinticInOut',
  label: {
    normal: {
      show: true,
      textStyle: {
        fontSize: 12
      }
    }
  },
  legend: {
    show: true,
    data: ['Country', 'Province', 'City', 'District', 'Street', 'Region', 'Statistics', 'Proxy'],
    textStyle: {
      color: '#000'
    },
    icon: 'circle',
    type: 'scroll',
    orient: 'vertical',
    left: 'auto',
    top: 'auto',
    bottom: 'auto',
    itemWidth: 10,
    itemHeight: 10
  },
  series: [
    {
      type: 'graph',
      layout: 'force',
      symbolSize: 45,
      focusNodeAdjacency: false, // 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
      roam: true, // 是否开启鼠标缩放和平移漫游
      draggable: true, // 是否可拖拽
      label: {
        show: true,
        fontSize: 12
      },
      force: {
        repulsion: 1000,
        friction: 0.2,
        gravity: 0.1
      },
      edgeSymbol: ['circle', 'arrow'], // 设置边两端的形状
      edgeSymbolSize: [1, 10],
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            fontSize: 10
          },
          formatter: '{c}'
        }
      },
      lineStyle: {
        normal: {
          opacity: 0.9,
          width: 1,
          curveness: 0
        }
      },
      categories: [
        {
          name: 'Country'
        },
        {
          name: 'Province'
        },
        {
          name: 'City'
        },
        {
          name: 'District'
        },
        {
          name: 'Street'
        },
        {
          name: 'Region'
        },
        {
          name: 'Statistics'
        },
        {
          name: 'Proxy'
        }
      ],
      data: null,
      links: null
    }
  ]
};