import * as cdk from '@aws-cdk/core';
import * as logs from '@aws-cdk/aws-logs';
import * as iam from '@aws-cdk/aws-iam';
import * as cr from '@aws-cdk/custom-resources';

export class customResource extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const onEvent = new lambda.Function(this, 'MyHandler', { /* ... */ });
        const myRole = new iam.Role(this, 'MyRole', { /* ... */ });
        
        const myProvider = new cr.Provider(this, 'MyProvider', {
            onEventHandler: onEvent,
            isCompleteHandler: isComplete,        // optional async "waiter"
            logRetention: logs.RetentionDays.ONE_DAY,   // default is INFINITE
            role: myRole, // must be assumable by the `lambda.amazonaws.com` service principal
        });

        new cdk.CustomResource(this, 'Resource1', { serviceToken: myProvider.serviceToken });
        new cdk.CustomResource(this, 'Resource2', { serviceToken: myProvider.serviceToken });

    }
}