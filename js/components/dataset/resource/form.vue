<style lang="less">
@gray-lighter: darken(#fff, 10%);

.actions-list {
    .list-group-item {
        @base-color: #eaeaea;
        @base-size: 60px;
        @border-size: 4px;
        height: @base-size + 2 * @border-size;
        background-color: lighten(@gray-lighter, 5%);
        margin: 0px 0px 10px;
        border-radius: 0px;
        border: @border-size solid transparent;
        padding: 0;

        .action-icon {
            float: left;
            width: @base-size;
            height: @base-size;
            background-color: lighten(#03496F, 10%);
            margin: 0px;

            span {
                color: lighten(@gray-lighter, 10%);
                line-height: 60px;
                text-align: center;
                display: block;
            }
        }

        .list-group-item-text {
            margin-left: @base-size + 10px;
            font-weight: normal;
        }

        .list-group-item-heading {
            margin-left: @base-size + 10px;
            margin-top: 9px;
            margin-bottom: 3px;
            font-weight: bold;
        }

        &:hover {
            background-color: @gray-lighter;

            .action-icon {
                background-color: lighten(@gray-lighter, 5%);
            }
        }
    }
}
</style>

<template>
<div class="list-group actions-list" v-if="!resource.type">
    <a v-repeat="actions" class="list-group-item pointer" v-on="click: set_type(type)">
        <div class="action-icon">
            <span class="fa fa-3x fa-{{icon}}"></span>
        </div>
        <h4 class="list-group-item-heading">
            {{ label }}
        </h4>
         <p class="list-group-item-text ellipsis">
        {{ details }}
        </p>
    </a>
</div>
<file-form v-if="resource.type == 'file'" v-ref="fileform"></file-form>
<remote-form v-if="resource.type == 'remote'" v-ref="remoteform"></remote-form>
<api-form v-if="resource.type == 'api'" v-ref="apiform"></api-form>
</template>

<script>
'use strict';

var Dataset = require('models/dataset'),
    Resource = require('models/resource');

module.exports = {
    props: ['dataset', 'resource'],
    data: function() {
        return {
            dataset: new Dataset(),
            resource: new Resource(),
            actions: [{
                label: this._('Local file'),
                details: this._('Send a file from your computer'),
                icon: 'cloud-upload',
                type: 'file'
            }, {
                label: this._('Online file'),
                details: this._('Register an already online file'),
                icon: 'cloud',
                type: 'remote'
            }, {
                label: this._('API'),
                details: this._('Register an API to access data'),
                icon: 'puzzle-piece',
                type: 'api'
            }],
        };
    },
    computed: {
        $form: function() {
            if (this.resource.type === 'file') {
                return this.$.fileform;
            } else if (this.resource.type === 'remote') {
                return this.$.remoteform.$.form;
            } else if (this.resource.type === 'api') {
                return this.$.apiform.$.form;
            }
        }
    },
    components: {
        'file-form': require('components/dataset/resource/file-form.vue'),
        'remote-form': require('components/dataset/resource/remote-form.vue'),
        'api-form': require('components/dataset/resource/api-form.vue')
    },
    methods: {
        set_type: function(type) {
            this.resource.type = type;
        },
        serialize: function() {
            return this.$form.serialize();
        },
        validate: function() {
            return this.$form ? this.$form.validate() : true;
        }
    }
};
</script>